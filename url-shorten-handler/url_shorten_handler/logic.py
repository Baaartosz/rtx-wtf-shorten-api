import json
import os

import boto3
import httpx
import shortuuid
from pydantic import ValidationError

from url_shorten_handler.model.shortened_url import ShortenedUrl
from url_shorten_handler.utils import get_proxy_param


def handle_post_url(event):
    request_body = json.loads(event["body"])
    try:
        short_url = ShortenedUrl(
            id=shortuuid.uuid(),
            original_url=request_body["url"],
        )
        print(f"Shortened URL: {short_url.model_dump_json()}")
    except KeyError:
        print(
            f"Failed to create shortened, due to url parameter missing. {request_body}"
        )
        return {
            "statusCode": 400,
            "body": "Body missing 'url' parameter",
        }
    except ValidationError:
        print(f"Failed to create shortened URL for request: {request_body}")
        return {
            "statusCode": 400,
            "body": f"Invalid URL: {request_body['url']}",
        }

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    table.put_item(
        Item=json.loads(short_url.model_dump_json()),
    )

    print(f"Saved to DynamoDB: {short_url.model_dump_json()}")
    return {
        "statusCode": 200,
        "body": short_url.model_dump_json(),
    }


def handle_get_url(event: dict):
    short_url_id = get_proxy_param(event)
    print(f"id: {short_url_id}")

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    short_url_item = table.get_item(Key={"id": short_url_id})

    if "Item" not in short_url_item:
        print(f"No Items found wih id: {short_url_id}")
        return {
            "statusCode": 404,
            "body": "Not found",
        }

    # todo optimise same ip address by changing to dictionary and incrementing same addresses
    source_ip = event.get("requestContext").get("http").get("sourceIp")
    table.update_item(
        Key={"id": short_url_id},
        UpdateExpression="SET #addresses = list_append(if_not_exists(#addresses, :empty_list), :new_address)",
        ExpressionAttributeNames={"#addresses": "addresses"},
        ExpressionAttributeValues={
            ":new_address": [source_ip],
            ":empty_list": [],
        },
    )
    print(f"Appended '{source_ip}' to url")

    print(f"Returning URL: {short_url_item['Item']['original_url']}")
    return {
        "statusCode": 308,
        "headers": {
            "Location": short_url_item["Item"]["original_url"],
        },
    }


def handle_delete_url(event):
    short_url_id = get_proxy_param(event)
    print(f"id: {short_url_id}")

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    short_url_item = table.delete_item(Key={"id": short_url_id})
    print(f"Item: {short_url_item}")
    return {
        "statusCode": 204,
    }


def handle_get_url_stats(event):
    short_url_id = get_proxy_param(event)
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    short_url_item = table.get_item(Key={"id": get_proxy_param(event)})["Item"]

    obj = ShortenedUrl(**short_url_item)
    print(f"Short URL: {obj.model_dump_json()}")

    if not obj.addresses:
        response_list = []
        chunks = [obj.addresses[i : i + 100] for i in range(0, len(obj.addresses), 100)]
        for chunk in chunks:
            formatted_batch_ips = [
                {
                    "query": ip,
                    "fields": "city,country,countryCode,mobile,proxy,hosting",
                }
                for ip in chunk
            ]
            response = httpx.post(
                url="http://ip-api.com/batch",
                json=formatted_batch_ips,
            )
            response_list.append(response.json())

        aggregated_data = {
            **obj.country_stats,
            **{
                k: v for k, v in obj.country_stats.items() if k not in obj.country_stats
            },
        }

        print(response_list)
        # Iterate over each entry in the country_stats list
        for entry in response_list[0]:
            country = entry["country"]

            # If the country is not yet in the aggregated_data dictionary, initialize it
            if country not in aggregated_data:
                aggregated_data[country] = {
                    "clicks": 0,
                }

            # Increment the total count for the country
            aggregated_data[country]["clicks"] += 1

        obj.addresses = []
        obj.country_stats = aggregated_data

        table.update_item(
            Key={"id": short_url_id},
            UpdateExpression="REMOVE #addresses SET #country_stats = :country_stats_value",
            ExpressionAttributeNames={
                "#addresses": "addresses",
                "#country_stats": "country_stats",
            },
            ExpressionAttributeValues={":country_stats_value": obj.country_stats},
        )

    return {"statusCode": 200, "body": obj.model_dump_json()}

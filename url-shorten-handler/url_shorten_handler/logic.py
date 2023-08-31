import json
import os

import boto3
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


def handle_get_url(event):
    short_url_id = get_proxy_param(event)
    print(f"id: {short_url_id}")

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    short_url_item = table.get_item(Key={"id": short_url_id})

    if "Item" not in short_url_item:
        print(f"No Items found with id: {short_url_id}")
        return {
            "statusCode": 404,
            "body": "Not found",
        }

    # todo when retrieving short_url,
    #  todo append the IP address
    #   (storing ip addresses probs isnt that bad but will need to do batch ip-address call)
    #              OR
    #  todo call ip-api and get country
    #   (api-call limits / will it slow down url retrival? or send it to another lambda to process)
    #              AND
    #   then append to object.

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


# todo handle aws pydantic lists that are supported in dyanmodb
# todo importing and exporting of model into and out of dynamodb
# call ip api http://ip-api.com/json/{ip}
# save location to object


def handle_get_url_stats(event):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    short_url_item = table.get_item(Key={"id": get_proxy_param(event)})["Item"]

    print(f"Item: {json.dumps(short_url_item)}")

    obj = ShortenedUrl(**short_url_item)
    print(obj)

    return {"statusCode": 200, "body": json.dumps(short_url_item)}

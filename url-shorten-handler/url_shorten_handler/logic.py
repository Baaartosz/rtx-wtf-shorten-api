import json
import os

import boto3
import shortuuid
from boto3.dynamodb.conditions import Attr
from pydantic import ValidationError

from url_shorten_handler.util.ip_processor import IPAddressProcessor
from url_shorten_handler.model.shortened_url import ShortenedUrl
from url_shorten_handler.util import logging
from url_shorten_handler.util.event_util import get_proxy_param


def handle_options(event: dict):
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "https://shorten.rtx.wtf, https://rtx.wtf",
            "Access-Control-Allow-Methods": "OPTIONS, GET, POST, DELETE",
            "Access-Control-Allow-Headers": "*",
        },
    }


def handle_post_url(event: dict):
    dynamodb = boto3.resource("dynamodb", region_name=os.getenv("AWS_REGION"))
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    request_body = json.loads(event["body"])
    try:
        short_url = ShortenedUrl(
            id=shortuuid.uuid(),
            original_url=request_body["url"],
        )
        logging.info(f"Shortened URL: {short_url.model_dump_json()}")
    except KeyError:
        logging.error(f"Failed to create shortened url, due to url parameter missing. {request_body}")
        return {
            "statusCode": 400,
            "body": "Body missing 'url' parameter",
        }
    except ValidationError:
        logging.error(f"Failed to create shortened URL for request: {request_body}")
        return {
            "statusCode": 400,
            "body": f"Invalid URL: {request_body['url']}",
        }
    except Exception as e:
        logging.fatal(f"Fatal exception occurred for request: {request_body}, {e}")
        return {
            "statusCode": 500,
            "body": f"Internal Server Error",
        }
    else:
        table.put_item(
            Item=json.loads(short_url.model_dump_json()),
        )

        logging.info(f"Saved to DynamoDB: {short_url.model_dump_json()}")
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "https://shorten.rtx.wtf, https://rtx.wtf",
                "Access-Control-Allow-Methods": "OPTIONS, GET, POST, DELETE",
                "Access-Control-Allow-Headers": "*",
            },
            "body": json.dumps(
                {
                    "id": short_url.id,
                    "url": f"https://rtx.wtf/s/{short_url.id}",
                }
            ),
        }


def handle_get_url(event: dict):
    dynamodb = boto3.resource("dynamodb", region_name=os.getenv("AWS_REGION"))
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    short_url_id = get_proxy_param(event)
    logging.info(f"Received '{short_url_id}' id for url retrieval")

    short_url_item = table.get_item(Key={"id": short_url_id}).get("Item")
    if short_url_item is None:
        logging.warn(f"No short url found with id: {short_url_id}")
        return {
            "statusCode": 308,
            "headers": {
                "Location": "https://shorten.rtx.wtf/404",
            },
        }

    try:
        source_ip = event.get("requestContext").get("http").get("sourceIp")
        logging.info(f"Updating '{short_url_id}' record with '{source_ip}' source ip")
        table.update_item(
            Key={"id": short_url_id},
            UpdateExpression="SET #addresses = list_append(if_not_exists(#addresses, :empty_list), :new_address)",
            ExpressionAttributeNames={"#addresses": "addresses"},
            ExpressionAttributeValues={
                ":new_address": [source_ip],
                ":empty_list": [],
            },
        )
        logging.info(f"Successfully appended '{source_ip}' to '{short_url_id}'")
    except Exception as ex:
        logging.error(f"Exception occurred during source_ip append, {ex}")

    logging.info(f"Returning URL: {short_url_item['original_url']}")
    return {
        "statusCode": 308,
        "headers": {
            "Location": short_url_item["original_url"],
        },
    }


def handle_delete_url(event: dict):
    dynamodb = boto3.resource("dynamodb", region_name=os.getenv("AWS_REGION"))
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    short_url_id = get_proxy_param(event)
    logging.info(f"Received '{short_url_id}' id for deletion")
    try:
        table.delete_item(
            Key={"id": short_url_id},
            ConditionExpression=Attr("id").exists(),
        )
        print(f"URL '{short_url_id}' deleted")
    except dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
        print(f"URL '{short_url_id}' does not exist")
    return {
        "statusCode": 204,
    }


def handle_get_url_stats(event):
    dynamodb = boto3.resource("dynamodb", region_name=os.getenv("AWS_REGION"))
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    short_url_id = get_proxy_param(event)
    logging.info(f"Received '{short_url_id}' id for stat retrieval")

    short_url_item = table.get_item(Key={"id": get_proxy_param(event)}).get("Item")

    if short_url_item is None:
        logging.warn(f"No Items found wih '{short_url_id}' id")
        return {
            "statusCode": 404,
        }

    short_url_object = ShortenedUrl(**short_url_item)
    logging.info(f"Loaded '{short_url_id}' into short url model: {short_url_object.model_dump_json()}")

    if len(short_url_object.addresses) != 0:
        logging.info(f"Object has {len(short_url_object.addresses)} ip addresses")
        ip_processor = IPAddressProcessor()
        country_clicks = ip_processor.process_ip_addresses(addresses=short_url_object.addresses)

        short_url_object.addresses = []
        short_url_object.country_stats = ip_processor.aggregate_dicts(
            country_clicks,
            short_url_object.country_stats,
        )

        try:
            table.update_item(
                Key={"id": short_url_id},
                UpdateExpression="REMOVE #addresses SET #country_stats = :country_stats_value",
                ExpressionAttributeNames={
                    "#addresses": "addresses",
                    "#country_stats": "country_stats",
                },
                ExpressionAttributeValues={":country_stats_value": short_url_object.country_stats},
            )
        except Exception as ex:
            logging.error(f"Failed to update record '{short_url_id}' with new data, {ex}")

    logging.info(f"Final short url object: {short_url_object.model_dump_json()}")
    return {
        "statusCode": 200,
        "body": short_url_object.model_dump_json(exclude={"addresses"}),
    }

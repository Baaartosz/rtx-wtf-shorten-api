import json
import os

import boto3
import shortuuid

from url_shorten_handler.model.shortened_url import ShortenedUrl
from url_shorten_handler.utils import get_proxy_param


def post_url(event, context):
    body = json.loads(event["body"])
    short_url = ShortenedUrl(
        id=shortuuid.uuid(),
        original_url=body["url"],
    )

    print(f"Shortened URL: {short_url.model_dump_json()}")

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


def get_url(event, context):
    short_url_id = get_proxy_param(event)
    print(f"id: {short_url_id}")

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    short_url_item = table.get_item(Key={"id": short_url_id})
    print(f"Item: {short_url_item}")

    if "Item" not in short_url_item:
        print(f"No Items found with id: {short_url_id}")
        return {
            "statusCode": 404,
            "body": "Not found",
        }

    print(f"Returning URL: {short_url_item['Item']['original_url']}")
    return {
        "statusCode": 308,
        "headers": {
            "Location": short_url_item["Item"]["original_url"],
        },
    }


def delete_url(event, context):
    short_url_id = get_proxy_param(event)
    print(f"id: {short_url_id}")

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    short_url_item = table.delete_item(Key={"id": short_url_id})
    print(f"Item: {short_url_item}")
    return {
        "statusCode": 204,
    }


def get_url_stats():
    return "Logic for GET url stats"

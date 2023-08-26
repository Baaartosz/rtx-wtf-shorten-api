import json
import os

import boto3
import shortuuid

from url_shorten_handler.model.shortened_url import ShortenedUrl
from url_shorten_handler.utils import get_proxy_param


def post_url(event, context):
    print(event)

    body = json.loads(event["body"])
    short_url = ShortenedUrl(
        id=shortuuid.uuid(),
        original_url=body["url"],
    )

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    table.put_item(
        Item=json.loads(short_url.model_dump_json()),
    )

    return {
        "statusCode": 200,
        "body": short_url.model_dump_json(),
    }


def get_url(event, context):
    short_url_id = get_proxy_param(event)

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    short_url_item = table.get_item(Key={"id": short_url_id})

    if "Item" not in short_url_item:
        return {
            "statusCode": 308,
            "body": "Link has been removed",
        }

    return {
        "statusCode": 308,
        "headers": {
            "Location": short_url_item["Item"]["original_url"],
        },
    }


def get_url_stats():
    return "Logic for GET url stats"

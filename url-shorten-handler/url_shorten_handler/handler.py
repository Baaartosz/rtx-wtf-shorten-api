import json
import os

import boto3
import shortuuid

from url_shorten_handler.logic import post_url, get_url, get_url_stats, delete_url
from url_shorten_handler.model.shortened_url import ShortenedUrl
from url_shorten_handler.utils import get_route_path


def lambda_handler(event, context):
    print(event)
    route, path = get_route_path(event)
    if route == "POST" and path == "/url":
        return post_url(event, context)
    elif route == "GET" and path == "/url/{proxy+}" or path == "/{proxy+}":
        return get_url(event, context)
    elif route == "DELETE" and path == "/url/{proxy+}":
        return delete_url(event, context)
    elif route == "GET" and path == "/url/stats/{proxy+}":
        return get_url_stats()
    else:
        return f"Not implemented -> {event['routeKey']}"


def old_code(event, context):
    print(event)

    body = json.loads(event["body"])
    print(body)
    short_url = ShortenedUrl(id=shortuuid.uuid(), original_url=body["url"])

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["SHORTEN_URLS_TABLE"])
    table.put_item(Item=json.loads(short_url.model_dump_json()))

    # fixme unsupported Type URL

    return {"statusCode": 200, "body": short_url.model_dump_json()}

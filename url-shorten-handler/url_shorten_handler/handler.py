from url_shorten_handler.logic import (
    handle_post_url,
    handle_get_url,
    handle_get_url_stats,
    handle_delete_url,
)
from url_shorten_handler.util.event_util import get_route_path


def lambda_handler(event, context):
    print(f"Event: {event}")
    handlers = {
        ("POST", "/url"): handle_post_url,
        ("GET", "/{proxy+}"): handle_get_url,
        ("GET", "/url/{proxy+}"): handle_get_url,
        ("DELETE", "/url/{proxy+}"): handle_delete_url,
        ("GET", "/url/stats/{proxy+}"): handle_get_url_stats,
    }
    handler = handlers.get(get_route_path(event), handle_not_implemented)
    return handler(event)


def handle_not_implemented(event):
    return f"Not implemented -> {event['routeKey']}"

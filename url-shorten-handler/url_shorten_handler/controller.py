from url_shorten_handler.logic import (
    handle_post_url,
    handle_get_url,
    handle_get_url_stats,
    handle_delete_url,
    handle_options, handle_list_url,
)
from url_shorten_handler.util.event_util import get_route_path


class UrlShortenerController:
    _ROUTE_MAP = {
        ("POST", "/url"): handle_post_url,
        ("OPTIONS", "/url"): handle_options,
        ("GET", "/url/list"): handle_list_url,
        ("GET", "/{proxy+}"): handle_get_url,
        # ("GET", "/url/{proxy+}"): handle_get_url,
        ("DELETE", "/url/{proxy+}"): handle_delete_url,
        ("GET", "/url/stats/{proxy+}"): handle_get_url_stats,
    }

    @classmethod
    def route_request(cls, event):
        return cls._ROUTE_MAP.get(get_route_path(event), cls._handle_not_implemented)

    @staticmethod
    def _handle_not_implemented(event):
        return f"Not implemented -> {event['routeKey']}"

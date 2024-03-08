from url_shorten_handler.logic import (
    handle_post_url,
    handle_get_url,
    handle_get_url_stats,
    handle_delete_url,
    handle_options,
    handle_list_url,
)
from url_shorten_handler.util.event_util import get_route_path


class UrlShortenerController:
    _ROUTE_MAP = {
        ("POST", "/urls"): handle_post_url,
        ("OPTIONS", "/urls"): handle_options,
        ("GET", "/users/{username}/urls"): handle_list_url,
        ("GET", "/{id+}"): handle_get_url,
        ("DELETE", "/urls"): handle_delete_url,
        ("GET", "/stats/{id+}"): handle_get_url_stats,
    }

    @classmethod
    def route_request(cls, event):
        return cls._ROUTE_MAP.get(get_route_path(event), cls._handle_not_implemented)

    @staticmethod
    def _handle_not_implemented(event):
        return f"Not implemented -> {event['routeKey']}"

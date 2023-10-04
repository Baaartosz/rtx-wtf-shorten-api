from typing import Tuple


def get_route_path(event) -> Tuple[str, str]:
    route_key: str = event["routeKey"]
    route_split = route_key.split(" ")
    return route_split[0], route_split[1]


def get_proxy_param(event) -> str:
    return event["pathParameters"]["proxy"].lstrip("s/")

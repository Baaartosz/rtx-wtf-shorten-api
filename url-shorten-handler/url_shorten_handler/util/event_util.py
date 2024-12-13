from typing import Tuple


def get_route_path(event) -> Tuple[str, str]:
    route_key: str = event["routeKey"]
    route_split = route_key.split(" ")
    return route_split[0], route_split[1]


def get_id_from_event(event) -> str:
    return event["pathParameters"]["id"].split("/")[-1]


def get_cognito_name(event) -> str:
    return event["requestContext"]["authorizer"]["jwt"]["claims"]["cognito:username"]

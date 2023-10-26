from url_shorten_handler.controller import UrlShortenerController
from url_shorten_handler.util.exception_decorator import exception_traceback


@exception_traceback
def lambda_handler(event, context):
    print(f"Event: {event}")
    handler = UrlShortenerController.route_request(event)
    return handler(event)

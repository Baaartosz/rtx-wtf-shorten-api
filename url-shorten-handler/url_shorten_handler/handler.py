from url_shorten_handler.controller import UrlShortenerController


def lambda_handler(event, context):
    print(f"Event: {event}")
    handler = UrlShortenerController.route_request(event)
    return handler(event)

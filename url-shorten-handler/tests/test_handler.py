from assertpy import assert_that

from url_shorten_handler.handler import lambda_handler
from tests.fixtures.requests import api_gw_request


def test_happy_path():
    raw_request = api_gw_request()
    response = lambda_handler(raw_request, None)
    assert_that(response).is_equal_to(
        {
            "statusCode": 200,
        }
    )
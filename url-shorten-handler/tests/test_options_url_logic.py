import os

import pytest
from assertpy import assert_that

from tests.fixtures.requests import api_gw_request_options_url
from url_shorten_handler.logic import handle_options


def test_happy_handle_options_url(
    mock_dynamo_db,
):
    response = handle_options(api_gw_request_options_url())

    # Assert that response is 308 and redirects to original_url
    assert_that(response["statusCode"]).is_equal_to(200)
    assert_that(response["headers"]).contains(
        "Access-Control-Allow-Origin",
        "Access-Control-Allow-Methods",
        "Access-Control-Allow-Headers",
    )

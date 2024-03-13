import os

import pytest
from assertpy import assert_that
from tests.fixtures.api_gw_event import get_urls, get_urls_from_domain

from tests.fixtures.requests import api_gw_request_from_rtx_wtf, api_gw_request_get_url
from url_shorten_handler.logic import handle_get_url


@pytest.mark.parametrize(
    "event",
    [
        pytest.param(get_urls()),
        pytest.param(get_urls_from_domain()),
    ],
    ids=["default_get_url", "alias_get_url"],
)
def test_happy_handle_get_url(
    event: dict,
    mock_dynamo_db,
):
    # Pre-populate DynamoDB table with test record
    table = _get_table(mock_dynamo_db)
    table.put_item(
        Item={
            "id": "oRtPrwjaSit",
            "original_url": "http://example.com",
        }
    )

    response = handle_get_url(event)

    # Assert that response is 308 and redirects to original_url
    assert_that(response["statusCode"]).is_equal_to(308)
    assert_that(response["headers"]["Location"]).is_equal_to("http://example.com")

    # Assert that IP address was logging for statistics
    short_url_item = table.get_item(Key={"id": "oRtPrwjaSit"})
    assert_that(short_url_item["Item"]["addresses"]).contains("82.21.32.80")


@pytest.mark.parametrize(
    "event",
    [
        pytest.param(get_urls()),
        pytest.param(get_urls_from_domain()),
    ],
    ids=["default_get_url", "alias_get_url"],
)
def test_unhappy_no_shortened_url(
    event: dict,
    mock_dynamo_db,
):
    response = handle_get_url(event)

    # Assert that response is 308 and redirects to shorten.rtx.wtf/404
    assert_that(response["statusCode"]).is_equal_to(308)
    assert_that(response["headers"]["Location"]).is_equal_to("https://shorten.rtx.wtf/404")


def _get_table(mock_dynamo_db):
    return mock_dynamo_db.Table(os.getenv("SHORTEN_URLS_TABLE"))

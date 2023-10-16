import os

import pytest
from assertpy import assert_that

from tests.fixtures.requests import api_gw_request_from_rtx_wtf, api_gw_request_get_url
from url_shorten_handler.logic import handle_get_url


@pytest.mark.parametrize(
    "event",
    [
        pytest.param(api_gw_request_get_url()),
        pytest.param(api_gw_request_from_rtx_wtf()),
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
            "id": "G3rZi26WMeGnqVvuNSnENu",
            "original_url": "http://example.com",
        }
    )

    response = handle_get_url(event)

    # Assert that response is 308 and redirects to original_url
    assert_that(response["statusCode"]).is_equal_to(308)
    assert_that(response["headers"]["Location"]).is_equal_to("http://example.com")

    # Assert that IP address was logging for statistics
    short_url_item = table.get_item(Key={"id": "G3rZi26WMeGnqVvuNSnENu"})
    assert_that(short_url_item["Item"]["addresses"]).contains("78.150.27.179")


@pytest.mark.parametrize(
    "event",
    [
        pytest.param(api_gw_request_get_url()),
        pytest.param(api_gw_request_from_rtx_wtf()),
    ],
    ids=["default_get_url", "alias_get_url"],
)
def test_missing_short_url_entry_handle_get_url(
    event: dict,
    mock_dynamo_db,
):
    response = handle_get_url(event)

    # Assert that response is 404 when id doesn't match anything in DynamoDB
    assert_that(response["statusCode"]).is_equal_to(404)
    assert_that(response["body"]).is_equal_to("Not found")


def _get_table(mock_dynamo_db):
    return mock_dynamo_db.Table(os.getenv("SHORTEN_URLS_TABLE"))

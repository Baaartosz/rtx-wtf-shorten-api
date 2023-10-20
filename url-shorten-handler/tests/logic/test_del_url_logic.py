import os

from assertpy import assert_that

from tests.fixtures.requests import api_gw_request_delete_url
from url_shorten_handler.logic import handle_delete_url


def test_happy_handle_delete_url(
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

    response = handle_delete_url(api_gw_request_delete_url())

    # Assert that response is 204 and delete short url
    assert_that(response["statusCode"]).is_equal_to(204)

    # Assert url no longer exists in DynamoDB
    short_url_item = table.get_item(Key={"id": "G3rZi26WMeGnqVvuNSnENu"})
    assert_that(short_url_item).does_not_contain_key("Item")


def test_empty_handle_delete_url(
    mock_dynamo_db,
):
    response = handle_delete_url(api_gw_request_delete_url())

    # Assert that response is 204 and delete short url
    assert_that(response["statusCode"]).is_equal_to(204)

    # Assert url no longer exists in DynamoDB
    table = _get_table(mock_dynamo_db)
    short_url_item = table.get_item(Key={"id": "G3rZi26WMeGnqVvuNSnENu"})
    assert_that(short_url_item).does_not_contain_key("Item")


def _get_table(mock_dynamo_db):
    return mock_dynamo_db.Table(os.getenv("SHORTEN_URLS_TABLE"))

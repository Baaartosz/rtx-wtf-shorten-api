import json
import os

import pytest
from assertpy import assert_that

from tests.fixtures.requests import api_gw_request_get_url_list_jwt
from url_shorten_handler.logic import handle_list_url


@pytest.mark.parametrize(
    "event",
    [
        pytest.param(api_gw_request_get_url_list_jwt()),
    ],
)
def test_happy_handle_get_url(
        event: dict,
        mock_dynamo_db,
):
    # Pre-populate DynamoDB table with test record
    table = _get_table(mock_dynamo_db)
    table.put_item(
        Item={
            "id": "oRtPrwjaSitz",
            "owner": "bart",
            "original_url": "http://example.com",
        }
    )
    table.put_item(
        Item={
            "id": "QRsdDXbeSJ3s",
            "owner": "bart",
            "original_url": "http://example.com",
        }
    )

    # Call the function under test
    response = handle_list_url(event)

    # Assert the structure and data of the response
    assert_that(response).is_not_none()
    assert_that(response).is_type_of(dict)


def _get_table(mock_dynamo_db):
    return mock_dynamo_db.Table(os.getenv("SHORTEN_URLS_TABLE"))

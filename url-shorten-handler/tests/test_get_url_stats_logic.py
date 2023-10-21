import json
import os

import pytest
from assertpy import assert_that
from pytest_httpx import HTTPXMock

from tests.fixtures.requests import api_gw_request_get_url_stats
from url_shorten_handler.logic import handle_get_url_stats


def _mock_ip_api_response(results: int) -> list:
    return [
        {
            "country": "United Kingdom",
            "query": "78.150.27.179",
        }
        for _ in range(results)
    ]


def _get_table(mock_dynamo_db):
    return mock_dynamo_db.Table(os.getenv("SHORTEN_URLS_TABLE"))


def test_happy_handle_get_url_stats_without_addresses(
    mock_dynamo_db,
):
    # Pre-populate DynamoDB table with test record
    table = _get_table(mock_dynamo_db)
    table.put_item(
        Item={
            "id": "G3rZi26WMeGnqVvuNSnENu",
            "original_url": "http://example.com",
            "country_stats": {
                "United Kingdom": 1,
            },
        }
    )

    response = handle_get_url_stats((api_gw_request_get_url_stats()))

    # Assert correct response has been returned
    assert_that(response["statusCode"]).is_equal_to(200)
    assert_that(response["body"]).is_equal_to(
        json.dumps(
            {
                "id": "G3rZi26WMeGnqVvuNSnENu",
                "original_url": "http://example.com/",
                "country_stats": {
                    "United Kingdom": "1",
                },
            },
            separators=(",", ":"),
        )
    )

    # Assert DynamoDB has not changed
    short_url_item = table.get_item(Key={"id": "G3rZi26WMeGnqVvuNSnENu"})
    assert_that(short_url_item["Item"].get("addresses")).is_none()
    assert_that(short_url_item["Item"]["country_stats"]).is_equal_to(
        {
            "United Kingdom": 1,
        }
    )


@pytest.mark.parametrize(
    "address_count, ip_api_response",
    [
        pytest.param(1, _mock_ip_api_response(1)),
        pytest.param(10, _mock_ip_api_response(10)),
        pytest.param(150, _mock_ip_api_response(150)),
    ],
    ids=["1 address", "10 addresses", "150 addresses"],
)
def test_happy_handle_get_url_stats_with_unprocessed_addresses(
    httpx_mock: HTTPXMock,
    address_count: int,
    ip_api_response: list,
    mock_dynamo_db,
):
    # Pre-populate DynamoDB table with test record
    table = _get_table(mock_dynamo_db)
    table.put_item(
        Item={
            "id": "G3rZi26WMeGnqVvuNSnENu",
            "original_url": "http://example.com",
            "addresses": ["78.150.27.179" for _ in range(address_count)],
        }
    )
    # Mock response from ip-api.com
    httpx_mock.add_response(
        url="http://ip-api.com/batch",
        method="POST",
        status_code=200,
        json=ip_api_response,
    )

    response = handle_get_url_stats((api_gw_request_get_url_stats()))

    # Assert DynamoDB has changed with valid amount of clicks
    assert_that(response["statusCode"]).is_equal_to(200)
    assert_that(response["body"]).is_equal_to(
        json.dumps(
            {
                "id": "G3rZi26WMeGnqVvuNSnENu",
                "original_url": "http://example.com/",
                "country_stats": {
                    "United Kingdom": address_count,
                },
            },
            separators=(",", ":"),
        )
    )

    # Assert correct response has been returned
    short_url_item = table.get_item(Key={"id": "G3rZi26WMeGnqVvuNSnENu"})
    assert_that(short_url_item["Item"].get("addresses")).is_none()
    assert_that(short_url_item["Item"]["country_stats"]).is_equal_to(
        {
            "United Kingdom": address_count,
        }
    )


def test_happy_handle_get_url_stats_with_existing_addresses(
    mock_dynamo_db,
    httpx_mock: HTTPXMock,
):
    # Pre-populate DynamoDB table with test record
    table = _get_table(mock_dynamo_db)
    table.put_item(
        Item={
            "id": "G3rZi26WMeGnqVvuNSnENu",
            "original_url": "http://example.com",
            "addresses": ["78.150.27.179"],
            "country_stats": {
                "United Kingdom": 1,
            },
        }
    )

    # Mock response from ip-api.com
    httpx_mock.add_response(
        url="http://ip-api.com/batch",
        method="POST",
        status_code=200,
        json=_mock_ip_api_response(1),
    )

    response = handle_get_url_stats((api_gw_request_get_url_stats()))

    # Assert correct response has been returned
    assert_that(response["statusCode"]).is_equal_to(200)
    assert_that(response["body"]).is_equal_to(
        json.dumps(
            {
                "id": "G3rZi26WMeGnqVvuNSnENu",
                "original_url": "http://example.com/",
                "country_stats": {
                    "United Kingdom": "2",
                },
            },
            separators=(",", ":"),
        )
    )

    # Assert DynamoDB has not changed
    short_url_item = table.get_item(Key={"id": "G3rZi26WMeGnqVvuNSnENu"})
    assert_that(short_url_item["Item"].get("addresses")).is_none()
    assert_that(short_url_item["Item"]["country_stats"]).is_equal_to(
        {
            "United Kingdom": 2,
        }
    )


def test_unhappy_no_short_url(
    mock_dynamo_db,
    httpx_mock: HTTPXMock,
):
    response = handle_get_url_stats((api_gw_request_get_url_stats()))

    # Assert correct response has been returned
    assert_that(response["statusCode"]).is_equal_to(404)

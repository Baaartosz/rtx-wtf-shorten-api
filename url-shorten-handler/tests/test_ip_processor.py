import httpx
import pytest
from assertpy import assert_that
from pytest_httpx import HTTPXMock

from url_shorten_handler.ip_processor.ip_processor import IPAddressProcessor


@pytest.mark.parametrize(
    "addresses, mock_api_response, expected_country_clicks",
    [
        pytest.param(
            ["78.150.27.179"],
            [
                {
                    "country": "United Kingdom",
                    "query": "78.150.27.179",
                }
            ],
            {
                "United Kingdom": 1,
            },
        ),
        pytest.param(
            [
                "78.150.27.179",
                "208.80.152.201",
                "8.8.8.8",
            ],
            [
                {
                    "country": "United Kingdom",
                    "query": "78.150.27.179",
                },
                {
                    "country": "United States",
                    "query": "208.80.152.201",
                },
                {
                    "country": "Canada",
                    "query": "8.8.8.8",
                },
            ],
            {
                "United Kingdom": 1,
                "United States": 1,
                "Canada": 1,
            },
        ),
        pytest.param(
            [
                "78.150.27.179",
                "208.80.152.201",
                "208.80.152.201",
                "208.80.152.201",
                "8.8.8.8",
                "8.8.8.8",
                "8.8.8.8",
                "8.8.8.8",
                "8.8.8.8",
            ],
            [
                {
                    "country": "United Kingdom",
                    "query": "78.150.27.179",
                },
                {
                    "country": "United States",
                    "query": "208.80.152.201",
                },
                {
                    "country": "Canada",
                    "query": "8.8.8.8",
                },
            ],
            {
                "United Kingdom": 1,
                "United States": 3,
                "Canada": 5,
            },
        ),
    ],
    ids=["One address", "Three addresses with single occurrence", "Three addresses with multiple occurrence"],
)
def test_happy_process_address(
    httpx_mock: HTTPXMock,
    addresses: list,
    mock_api_response: list,
    expected_country_clicks: dict,
):
    httpx_mock.add_response(
        url="http://ip-api.com/batch",
        method="POST",
        status_code=200,
        json=mock_api_response,
    )

    country_clicks = IPAddressProcessor().process_ip_addresses(addresses)
    assert_that(country_clicks).is_equal_to(expected_country_clicks)


@pytest.mark.parametrize(
    "address_count",
    [
        pytest.param(1),
        pytest.param(50),
        pytest.param(150),
    ],
)
def test_same_address_multiple_times(
    httpx_mock: HTTPXMock,
    address_count: int,
):
    httpx_mock.add_response(
        url="http://ip-api.com/batch",
        method="POST",
        status_code=200,
        json=[
            {
                "country": "United Kingdom",
                "query": "78.150.27.179",
            }
        ],
    )

    country_clicks = IPAddressProcessor().process_ip_addresses(["78.150.27.179" for _ in range(address_count)])
    assert_that(country_clicks).is_equal_to(
        {
            "United Kingdom": address_count,
        }
    )


def test_request_limited_api(
    httpx_mock: HTTPXMock,
):
    httpx_mock.add_response(
        url="http://ip-api.com/batch",
        method="POST",
        status_code=429,
    )

    country_clicks = IPAddressProcessor().process_ip_addresses(["78.150.27.179"])
    assert_that(country_clicks).is_equal_to({})


@pytest.mark.parametrize(
    "status_code",
    [
        pytest.param(500),
        pytest.param(503),
        pytest.param(504),
    ],
)
def test_5xx_api_errors(
    status_code: int,
    httpx_mock: HTTPXMock,
):
    httpx_mock.add_response(
        url="http://ip-api.com/batch",
        method="POST",
        status_code=status_code,
    )
    with pytest.raises(httpx.HTTPStatusError):
        IPAddressProcessor().process_ip_addresses(["78.150.27.179"])

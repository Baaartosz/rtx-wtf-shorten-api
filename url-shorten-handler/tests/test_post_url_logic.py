import json
import os

import pytest
import shortuuid
from assertpy import assert_that

from url_shorten_handler.logic import handle_post_url


@pytest.mark.parametrize(
    "test_url",
    [
        pytest.param("http://example.com/"),
        pytest.param("https://example.com/"),
        pytest.param("http://www.example.com/"),
        pytest.param("http://sub.example.com/"),
        pytest.param("https://example.com/path/to/resource/"),
        pytest.param("https://example.com/?query=value"),
        pytest.param("http://example.com/#fragment"),
        pytest.param("https://example.com/:8080"),
        pytest.param("http://user:password@example.com/"),
        pytest.param("http://example.com/path/to/resource?query=value#fragment"),
    ],
)
def test_happy_handle_post_url(
    test_url: str,
    static_shortuuid,
    mock_dynamo_db,
):
    # Mock event input
    event = {"body": json.dumps({"url": test_url})}

    # Call the function
    response = handle_post_url(event)

    # Assert the response
    assert_that(response["statusCode"]).is_equal_to(200)
    assert_that(json.loads(response["body"])).is_equal_to(
        {
            "id": static_shortuuid,
            "url": f"https://rtx.wtf/s/{static_shortuuid}",
        }
    )

    # Get reference to DynamoDB table
    table = mock_dynamo_db.Table(os.getenv("SHORTEN_URLS_TABLE"))

    # Query DynamoDB for the record
    result = table.get_item(Key={"id": static_shortuuid})

    # Check that the record exists and has the correct URL
    assert_that(result).contains_key("Item")
    assert_that(result["Item"]["original_url"]).is_equal_to(test_url)


@pytest.mark.parametrize(
    "test_url",
    [
        pytest.param("bad.url/"),
        pytest.param("example.dev/"),
        pytest.param("w_ww.ex_ample.co$m/"),
    ],
)
def test_malformed_handle_post_url(
    test_url: str,
    static_shortuuid,
    mock_dynamo_db,
):
    # Mock event input
    event = {"body": json.dumps({"url": test_url})}

    # Call the function
    response = handle_post_url(event)

    # Assert the response
    assert_that(response["statusCode"]).is_equal_to(400)
    assert_that(response["body"]).is_equal_to(f"Invalid URL: {test_url}")


def test_bad_request_handle_post_url(
    static_shortuuid,
    mock_dynamo_db,
):
    # Mock event input
    event = {"body": json.dumps({"bad": "field"})}

    # Call the function
    response = handle_post_url(event)

    # Assert the response
    assert_that(response["statusCode"]).is_equal_to(400)
    assert_that(response["body"]).is_equal_to("Body missing 'url' parameter")

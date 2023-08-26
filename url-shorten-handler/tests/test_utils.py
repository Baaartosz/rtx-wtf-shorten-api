import pytest
from assertpy import assert_that

from tests.fixtures.requests import (
    api_gw_request_post_url,
    api_gw_request_get_url,
    api_gw_request_get_url_stats,
)

from url_shorten_handler.utils import get_route_path, get_proxy_param


@pytest.mark.parametrize(
    "api_request, expected_route, expected_path",
    [
        (api_gw_request_post_url(), "POST", "/url"),
        (api_gw_request_get_url(), "GET", "/url/{proxy+}"),
        (api_gw_request_get_url_stats(), "GET", "/url/stats/{proxy+}"),
    ],
)
def test_get_route_path(api_request, expected_route, expected_path):
    route, path = get_route_path(api_request)
    assert_that(route).is_equal_to(expected_route)
    assert_that(path).is_equal_to(expected_path)


@pytest.mark.parametrize(
    "api_request, expected_id",
    [
        (api_gw_request_get_url(), "G3rZi26WMeGnqVvuNSnENu"),
        (api_gw_request_get_url_stats(), "G3rZi26WMeGnqVvuNSnENu"),
    ],
)
def test_get_proxy_param(api_request, expected_id):
    actual_id = get_proxy_param(api_request)
    assert_that(actual_id).is_equal_to(expected_id)

import pytest
from assertpy import assert_that

from tests.fixtures.requests import (
    api_gw_request_post_url,
    api_gw_request_get_url,
    api_gw_request_get_url_stats,
    api_gw_request_delete_url,
    api_gw_request_from_rtx_wtf,
    api_gw_request_from_rtx_wtf_alternative,
    api_gw_request_options_url,
    api_gw_request_get_url_shorten_rtx,
)

from url_shorten_handler.util.event_util import get_route_path, get_proxy_param, get_cognito_name


@pytest.mark.parametrize(
    "api_request, expected_route, expected_path",
    [
        (api_gw_request_post_url(), "POST", "/urls"),
        (api_gw_request_options_url(), "OPTIONS", "/urls"),
        (api_gw_request_get_url(), "GET", "/urls/{proxy+}"),
        (api_gw_request_delete_url(), "DELETE", "/urls/{id+}"),
        (api_gw_request_get_url_stats(), "GET", "/stats/{id+}"),
        (api_gw_request_from_rtx_wtf(), "GET", "/{id+}"),
        (api_gw_request_from_rtx_wtf_alternative(), "GET", "/{id+}"),
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
        (api_gw_request_from_rtx_wtf(), "G3rZi26WMeGnqVvuNSnENu"),
        (api_gw_request_from_rtx_wtf_alternative(), "G3rZi26WMeGnqVvuNSnENu"),
        (api_gw_request_get_url_shorten_rtx(), "G3rZi26WMeGnqVvuNSnENu"),
    ],
)
def test_get_proxy_param(api_request, expected_id):
    actual_id = get_proxy_param(api_request)
    assert_that(actual_id).is_equal_to(expected_id)


@pytest.mark.parametrize(
    "api_request, expected_name",
    [
        (api_gw_request_post_url(), "bart"),
    ],
)
def test_get_route_path(api_request, expected_name):
    name = get_cognito_name(api_request)
    assert_that(name).is_equal_to(expected_name)

import pytest
from assertpy import assert_that
from url_shorten_handler.util.event_util import (
    get_route_path,
    get_id_from_event,
    get_cognito_name,
)
from tests.fixtures.api_gw_event import (
    get_urls,
    get_urls_from_domain,
    post_urls,
    options_urls,
    del_urls,
)


@pytest.mark.parametrize(
    "api_request, expected_id",
    [
        (get_urls(), "oRtPrwjaSit"),
        (get_urls_from_domain(), "oRtPrwjaSit"),
    ],
)
def test_get_proxy_param(api_request, expected_id):
    actual_id = get_id_from_event(api_request)
    assert_that(actual_id).is_equal_to(expected_id)


@pytest.mark.parametrize(
    "api_request, expected_name",
    [
        (post_urls(), "bart"),
    ],
)
def test_get_route_path(api_request, expected_name):
    name = get_cognito_name(api_request)
    assert_that(name).is_equal_to(expected_name)


@pytest.mark.parametrize(
    "api_request, expected_route, expected_path",
    [
        (post_urls(), "POST", "/urls"),
        (options_urls(), "OPTIONS", "/urls"),
        (del_urls(), "DELETE", "/urls/{id+}"),
        (get_urls(), "GET", "/urls/{id+}"),
        (get_urls_from_domain(), "GET", "/{id+}"),
    ],
)
def test_get_route_path(api_request, expected_route, expected_path):
    route, path = get_route_path(api_request)
    print(f"{route} {path}")
    assert_that(route).is_equal_to(expected_route)
    assert_that(path).is_equal_to(expected_path)

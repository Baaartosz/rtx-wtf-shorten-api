"""
So I wrote this quickly with the general idea of creating a quick way to test that my
changes in the API continued to work. Essentially mimicking BDD
TODO convert to Gherkin Behave framework
"""
import json
import os
from functools import cache

import boto3
import pytest
import requests
from assertpy import *


@cache
def authorize():
    client = boto3.client("cognito-idp")
    try:
        response = client.admin_initiate_auth(
            UserPoolId=os.getenv("USER_POOL_ID"),
            ClientId=os.getenv("CLIENT_ID"),
            AuthFlow="ADMIN_USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": os.getenv("TEST_USER"),
                "PASSWORD": os.getenv("TEST_PWD"),
            },
        )

        id_token = response["AuthenticationResult"]["IdToken"]
        print("JWT Token:", id_token)
        return id_token
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


DOMAIN_URL = "https://rtx.wtf/s"
API_URL = "https://shorten.rtx.wtf/api"
UNIQUE_ID = ""


def assert_common_response_headers(response, allow_methods="OPTIONS, GET, POST, DELETE"):
    assert_that(response.headers.get("access-control-allow-headers")).is_equal_to("*")
    assert_that(response.headers.get("access-control-allow-origin")).is_equal_to("*")
    assert_that(response.headers.get("access-control-allow-methods")).is_equal_to(allow_methods)


@pytest.mark.order(1)
@pytest.mark.usefixtures("env_variables")
def test_create_new_url():
    print('POST /api/urls {"url": "https://media.tenor.com/d7VOr5nJ0W4AAAAC/cat-meme.gif"}')
    response = requests.post(
        url=API_URL + "/urls",
        headers={"Authorization": authorize()},
        json={"url": "https://media.tenor.com/d7VOr5nJ0W4AAAAC/cat-meme.gif"},
    )
    assert_that(response.status_code).is_equal_to(200)
    global UNIQUE_ID
    UNIQUE_ID = json.loads(response.text).get("id")
    print(f"UNIQUE_ID -> {UNIQUE_ID}")


@pytest.mark.order(2)
@pytest.mark.usefixtures("env_variables")
def test_options_for_urls_endpoint():
    print(f"OPTIONS /api/urls")
    response = requests.options(
        url=API_URL + "/urls",
    )
    assert_that(response.status_code).is_equal_to(200)
    assert_common_response_headers(response=response)


@pytest.mark.order(3)
@pytest.mark.usefixtures("env_variables")
def test_redirect_to_original_url_from_api():
    print(f"GET /api/urls/{UNIQUE_ID}")
    response = requests.get(
        url=API_URL + f"/urls/{UNIQUE_ID}",
    )
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.order(4)
@pytest.mark.usefixtures("env_variables")
def test_redirect_to_original_url_from_domain():
    print(f"GET /{UNIQUE_ID}")
    response = requests.get(
        url=DOMAIN_URL + f"/{UNIQUE_ID}",
    )
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.order(5)
@pytest.mark.usefixtures("env_variables")
def test_stats_for_url():
    print(f"GET /api/stats/{UNIQUE_ID}")
    response = requests.get(
        url=API_URL + f"/stats/{UNIQUE_ID}",
        headers={"Authorization": authorize()},
    )
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains_key("id", "original_url", "country_stats")
    assert_that(response.json().get("addresses")).is_none()


@pytest.mark.order(6)
@pytest.mark.usefixtures("env_variables")
def test_get_users_shortened_urls():
    print(f"GET /urls")
    response = requests.get(
        url=API_URL + f"/urls",
        headers={"Authorization": authorize()},
    )
    assert_that(response.status_code).is_equal_to(200)
    assert_common_response_headers(response=response, allow_methods="OPTIONS, GET")


@pytest.mark.order(7)
@pytest.mark.usefixtures("env_variables")
def test_options_for_urls_endpoint():
    print(f"OPTIONS /api/urls/{UNIQUE_ID}")
    response = requests.options(
        url=API_URL + f"/urls/{UNIQUE_ID}",
    )
    assert_that(response.status_code).is_equal_to(200)
    assert_common_response_headers(response=response)


@pytest.mark.order(8)
@pytest.mark.usefixtures("env_variables")
def test_delete_url():
    print(f"DEL /api/urls/{UNIQUE_ID}")
    response = requests.delete(
        url=API_URL + f"/urls/{UNIQUE_ID}",
        headers={"Authorization": authorize()},
    )
    assert_that(response.status_code).is_equal_to(204)

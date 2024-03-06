import os
from unittest.mock import patch

import boto3
import pytest
import shortuuid
from httpx import Client
from moto import mock_dynamodb


@pytest.fixture
def static_shortuuid(mocker):
    mocker.patch.object(shortuuid, "uuid", return_value="uniqueid")
    return "uniqueid"


@pytest.fixture
def environment_variables(monkeypatch):
    monkeypatch.setenv("AWS_REGION", "eu-west-2")
    monkeypatch.setenv("SHORTEN_URLS_TABLE", "rtx-wtf-shortened-urls")


@pytest.fixture
def mock_dynamo_db(environment_variables):
    with mock_dynamodb():
        boto_resource = boto3.resource("dynamodb", region_name=os.getenv("AWS_REGION"))
        table_name = os.getenv("SHORTEN_URLS_TABLE")

        # Create the DynamoDB table
        boto_resource.create_table(
            TableName=table_name,
            KeySchema=[
                {"AttributeName": "id", "KeyType": "HASH"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "id", "AttributeType": "S"},
                {"AttributeName": "owner", "AttributeType": "S"},
            ],
            GlobalSecondaryIndexes=[  # Define the Global Secondary Index
                {
                    "IndexName": "OwnerIndex",
                    "KeySchema": [
                        {"AttributeName": "owner", "KeyType": "HASH"},  # Key schema for the GSI
                    ],
                    "Projection": {
                        "ProjectionType": "ALL"
                    },
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 5,
                        "WriteCapacityUnits": 5,
                    },
                },
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )

        # Ensure the table is active
        boto_resource.Table(table_name).wait_until_exists()

        yield boto_resource

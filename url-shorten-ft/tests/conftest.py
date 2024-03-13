import os

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="session")
def env_variables():
    load_environment_variables()
    yield


def load_environment_variables():
    current_dir = os.getcwd()
    env_file_path = os.path.join(current_dir, "aws.env")
    load_dotenv(dotenv_path=env_file_path)

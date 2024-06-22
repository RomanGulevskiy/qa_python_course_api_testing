import pytest

from api_clients.dog_api_client import DogApiClient
from api_clients.open_brewery_db_api_client import OpenBreweryDBClient
from api_clients.jsonplaceholder_api_client import JSONPlaceholderClient


@pytest.fixture()
def dog_api_client():
    client = DogApiClient()
    return client


@pytest.fixture()
def open_brewery_db_client():
    client = OpenBreweryDBClient()
    return client


@pytest.fixture()
def jsonplaceholder_client():
    client = JSONPlaceholderClient()
    return client


def pytest_addoption(parser):
    parser.addoption("--url")
    parser.addoption("--status_code")


@pytest.fixture()
def test_data(request):
    url = request.config.getoption("--url")
    status_code = int(request.config.getoption("--status_code"))
    return {"url": url, "status_code": status_code}
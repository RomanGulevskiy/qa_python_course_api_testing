import pytest

from assertions.assertion_base import assert_schema

from models.open_brewery_db_model import OpenBreweryDBBaseModel
from models.open_brewery_db_model import OpenBreweryDBNegativeModel


def test_get_random_brewery(open_brewery_db_client):
    response = open_brewery_db_client.get_random_brewery()
    assert response.status_code == 200
    assert_schema(response, OpenBreweryDBBaseModel)


def test_get_list_of_all_breweries(open_brewery_db_client):
    response = open_brewery_db_client.get_list_of_all_breweries()
    assert response.status_code == 200
    assert_schema(response, OpenBreweryDBBaseModel)


@pytest.mark.parametrize(["brewery_type", "status_code"],
                         [("bar", 200),
                          ("regional", 200),
                          ("brewpub", 200),
                          ("large", 200)])
def test_get_list_of_breweries_by_type(open_brewery_db_client, brewery_type, status_code):
    response = open_brewery_db_client.get_list_of_breweries_by_type(brewery_type)
    assert response.status_code == status_code
    assert_schema(response, OpenBreweryDBBaseModel)


@pytest.mark.parametrize(["city", "status_code"],
                         [("san_diego", 200),
                          ("petaluma", 200),
                          ("denver", 200)])
def test_get_list_of_breweries_by_city(open_brewery_db_client, city, status_code):
    response = open_brewery_db_client.get_list_of_breweries_by_city(city)
    assert response.status_code == status_code
    assert_schema(response, OpenBreweryDBBaseModel)


@pytest.mark.parametrize(["brewery_id", "status_code"],
                         [("ef970757-fe42-416f-931d-722451f1f59c", 200),
                          ("9c5a66c8-cc13-416f-a5d9-0a769c87d318", 200),
                          ("34e8c68b-6146-453f-a4b9-1f6cd99a5ada", 200),
                          ("brewery", 404)])
def test_get_brewery_by_id(open_brewery_db_client, brewery_id, status_code):
    response = open_brewery_db_client.get_brewery_by_id(brewery_id)
    assert response.status_code == status_code
    if response.status_code == 200:
        assert_schema(response, OpenBreweryDBBaseModel)
    else:
        assert_schema(response, OpenBreweryDBNegativeModel)

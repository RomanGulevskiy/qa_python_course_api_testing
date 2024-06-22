import pytest

from assertions.assertion_base import assert_schema

from models.dog_api_model import DogApiBreedsListModel
from models.dog_api_model import DogApiBreedImagesModel
from models.dog_api_model import DogApiRandomImageModel
from models.dog_api_model import DogApiSubbreedsListModel


def test_get_random_image(dog_api_client):
    response = dog_api_client.get_random_image()
    assert response.status_code == 200
    assert_schema(response, DogApiRandomImageModel)


@pytest.mark.parametrize(["breed", "status_code"],
                         [("hound", 200),
                          ("stbernard", 200)])
def test_get_images_by_breed(dog_api_client, breed, status_code):
    response = dog_api_client.get_images_by_breed(breed)
    assert response.status_code == status_code
    assert_schema(response, DogApiBreedImagesModel)


@pytest.mark.parametrize(["breed", "status_code"],
                         [("hound", 200),
                          ("terrier", 200)])
def test_get_list_of_subbreeds(dog_api_client, breed, status_code):
    response = dog_api_client.get_list_of_subbreeds(breed)
    assert response.status_code == status_code
    assert_schema(response, DogApiSubbreedsListModel)


def test_get_list_of_all_breeds(dog_api_client):
    response = dog_api_client.get_list_of_all_breeds()
    assert response.status_code == 200
    assert_schema(response, DogApiBreedsListModel)


@pytest.mark.parametrize(["breed", "status_code"],
                         [("hound", 200),
                          ("terrier", 200),
                          ("some-breed", 404),
                          (123, 404),
                          ("", 404)])
def test_get_random_image_from_breed_collection(dog_api_client, breed, status_code):
    response = dog_api_client.get_random_image_from_breed_collection(breed)
    assert response.status_code == status_code
    assert_schema(response, DogApiRandomImageModel)

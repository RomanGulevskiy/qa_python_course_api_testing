from pydantic import BaseModel

from typing import Optional


class DogApiBaseModel(BaseModel):
    status: str
    code: Optional[int] = None


class DogApiRandomImageModel(DogApiBaseModel):
    message: str


class DogApiBreedsListModel(DogApiBaseModel):
    message: object


class DogApiBreedImagesModel(DogApiBaseModel):
    message: list


class DogApiSubbreedsListModel(DogApiBaseModel):
    message: list

from pydantic import BaseModel

from typing import Optional


class OpenBreweryDBBaseModel(BaseModel):
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    address_3: Optional[str] = None
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[str] = None
    latitude: Optional[str] = None
    phone: Optional[str] = None
    website_url: Optional[str] = None
    state: str
    street: Optional[str] = None


class OpenBreweryDBNegativeModel(BaseModel):
    message: str

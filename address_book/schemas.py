from pydantic import BaseModel, validator
import re
from .utils import validate_latitude, validate_longitude


class BaseAddreess(BaseModel):
    house: str
    street: str
    city: str
    postal_code: str
    state: str
    country: str
    latitude: float
    longitude: float


class CreateAddreess(BaseAddreess):
    @validator("postal_code")
    def postal_code_validation(cls, pcode: str):
        """
        The valid pin code of India must satisfy the following conditions.

            1] It can be only six digits.
            2] It should not start with zero.
            3] First digit of the pin code must be from 1 to 9.
            4] Next five digits of the pin code may range from 0 to 9.
            5] It should allow only one white space, but after three digits, although this is optional.

        regex = "^[1-9]{1}[0-9]{2}\\s{0, 1}[0-9]{3}$";

        ^ represents the starting of the number.
        [1-9]{1} represents the starting digit in the pin code ranging from 1 to 9.
        [0-9]{2} represents the next two digits in the pin code ranging from 0 to 9.
        \\s{0, 1} represents the white space in the pin code that can occur once or never.
        [0-9]{3} represents the last three digits in the pin code ranging from 0 to 9.
        $ represents the ending of the number.
        """
        if len(pcode) != 6:
            raise ValueError("must be six digits")

        regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
        rex = re.compile(regex)

        # Returns Re Obect if the pin code
        # matched the ReGex else None
        match = re.match(rex, pcode)
        if not match:
            raise ValueError("Invalid PinCode")

        return pcode

    @validator("latitude")
    def latitude_validation(cls, lat: float):
        """
        The latitude must be a number between -90 and 90 inclusive
        """
        try:
            if validate_latitude(lat):
                return lat
            raise ValueError(
                "Latitude Must be a Finite Number between -90 and 90 eg: 38.8951"
            )
        except Exception as e:
            raise ValueError(
                "Latitude Must be a Finite Number between -90 and 90 eg: 38.8951"
            )

    @validator("longitude")
    def longitude_validation(cls, lon: float):
        """
        The longitude must be a number between -180 and 180 inclusive
        """
        try:
            if validate_longitude(lon):
                return lon
            raise ValueError(
                "Longitude Must be a Finite Number between -180 and 180 eg: -77.0364"
            )
        except Exception as e:
            raise ValueError(
                "Longitude Must be a Finite Number between -180 and 180 eg: -77.0364"
            )


class ReadAddress(BaseAddreess):
    id: int

    class Config:
        orm_mode = True


class UpdateAddress(CreateAddreess):
    house: str | None = None
    street: str | None = None
    city: str | None = None
    postal_code: str | None = None
    state: str | None = None
    country: str | None = None
    latitude: float | None = None
    longitude: float | None = None

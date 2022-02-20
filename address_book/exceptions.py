class BaseError(Exception):
    pass


class AddressNotFoundError(BaseError):
    def __init__(self, id: int):
        self.status_code = 404  # Not Found
        self.detail = f"Address With Id = {id} Does Not Exists !"


class WrongValueError(BaseError):
    def __init__(self):
        self.status_code = 400  #  Bad Request
        self.detail = "Latitude must be a number between -90 and 90, Longitude must be a number between -180 and 180"

from geopy.distance import geodesic
import math


def get_distance_km(coordinate1: tuple, coordinate2: tuple) -> float:
    """
    parameters which are coordinates must be in a tuple of (lat, long)
    """
    distance = geodesic(coordinate1, coordinate2).km
    return abs(distance)


def validate_latitude(lat: float) -> bool:
    """
    The latitude must be a number between -90 and 90 inclusive
    """
    return math.isfinite(lat) and abs(lat) <= 90


def validate_longitude(lon: float) -> bool:
    """
    The longitude must be a number between -180 and 180 inclusive
    """
    return math.isfinite(lon) and abs(lon) <= 180

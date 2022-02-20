from sqlalchemy import Column, Integer, String, Float
from .database import Base
from sqlalchemy.ext.hybrid import hybrid_method
from .utils import get_distance_km


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    house = Column(String)
    street = Column(String)
    city = Column(String)
    postal_code = Column(Integer)
    state = Column(String)
    country = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    @hybrid_method
    def is_within_range(self, coordinate2: tuple, distance_range: float) -> bool:
        return (
            get_distance_km((self.latitude, self.longitude), coordinate2)
            <= distance_range
        )

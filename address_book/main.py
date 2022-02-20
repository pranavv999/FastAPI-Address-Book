from fastapi import FastAPI, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .exceptions import AddressNotFoundError, WrongValueError, MissingAllValues
from .utils import validate_longitude, validate_latitude


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

RESPONSE_MODEL = schemas.ReadAddress

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=list[RESPONSE_MODEL])
def index(db: Session = Depends(get_db)):
    db_addreeses = crud.get_addresses(db)
    return db_addreeses


@app.get("/address/{address_id}", response_model=RESPONSE_MODEL)
def get_address(
    address_id: int = Path(..., title="The ID of the address to get", ge=1),
    db: Session = Depends(get_db),
):
    try:
        db_address = crud.get_address(db, address_id)
        return db_address
    except AddressNotFoundError as e:
        raise HTTPException(**e.__dict__)


@app.get("/address", response_model=list[RESPONSE_MODEL])
def get_addresses_within_range(
    lat: float = Query(
        ...,
        title="Latitude",
        description="Latitude must be a finit number between -90 and 90",
    ),
    lon: float = Query(
        ...,
        title="Longitude",
        description="Longitude must be a finit number between -180 and 180",
    ),
    distance_range: float = Query(..., description="Distance in Kilometers"),
    db: Session = Depends(get_db),
):
    response = list()
    if not (validate_latitude(lat) and validate_longitude(lon)):
        raise HTTPException(**WrongValueError().__dict__)
    db_addresses = db.query(models.Address).all()
    for address in db_addresses:
        if address.is_within_range((lat, lon), distance_range):
            response.append(address)
    return response


@app.post("/create_address", response_model=RESPONSE_MODEL)
def create_address(address: schemas.CreateAddreess, db: Session = Depends(get_db)):
    return crud.create_address(db, address)


@app.patch("/address/{address_id}", response_model=RESPONSE_MODEL)
def update_address(
    address: schemas.UpdateAddress,
    db: Session = Depends(get_db),
    address_id: int = Path(..., title="The ID of the address to get", ge=1),
):
    if any(address.dict().values()):
        try:
            res = crud.update_address(db, address_id, address)
            return res.all()[0]
        except AddressNotFoundError as e:
            raise HTTPException(**e.__dict__)
    else:
        raise HTTPException(**MissingAllValues().__dict__)


@app.delete("/address/{address_id}")
def delete_address(
    address_id: int = Path(..., title="The ID of the address to get", ge=1),
    db: Session = Depends(get_db),
):
    try:
        return crud.delete_address(db, address_id)
    except AddressNotFoundError as e:
        raise HTTPException(**e.__dict__)

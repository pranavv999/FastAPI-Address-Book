from sqlalchemy.orm import Session
from . import models, schemas
from .exceptions import AddressNotFoundError


def get_addresses(db: Session):
    """
    Returns all Instances of Address
    """
    return db.query(models.Address).all()


def get_address(db: Session, address_id: int):
    """
    Returns Address Instance of matching address_id
    if not raise Not Found Exception
    """
    db_address = (
        db.query(models.Address).filter(models.Address.id == address_id).first()
    )

    if not db_address:
        raise AddressNotFoundError(address_id)

    return db_address


def create_address(db: Session, address: schemas.CreateAddreess):
    """
    Creates Address Instance with given address and returns
    """
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def delete_address(db: Session, address_id: int):
    """
    Delets Address Instance of given address_id if present
    if not raise Not Found Exception
    """
    db_address = get_address(db, address_id)
    db.delete(db_address)
    db.commit()
    return {
        "status": "Success",
        "message": f"Address with id = {address_id} deleted successfully.",
    }


def update_address(db: Session, address_id: int, address: schemas.UpdateAddress):
    """
    Updates Address Instance of given address_id with given address if present
    if not raise Not Found Exception
    """
    db_address = db.query(models.Address).filter(models.Address.id == address_id)
    if len(db_address.all()) < 1:
        raise AddressNotFoundError(address_id)
    db_address.update(address.dict(exclude_unset=True))
    db.commit()
    return db_address

from .init import get_db

from src.model.rider import Rider 
from error import Missing, Duplicate  # Assuming custom exceptions are defined
from sqlalchemy import exc
from .schemas import RiderBase  # Assuming schemas are defined

def get_all() -> list[RiderBase ]:
    db = next(get_db())
    return db.query(Rider).all()

def get_one(name: str) -> RiderBase :
    db = next(get_db())
    row = db.query(Rider).filter(Rider.name == name).first()
    if row:
        return row
    else:
        raise Missing(msg=f"Rider (name: {name}) not found")  

def create(Rider: RiderBase ) -> RiderBase :
    if not Rider:
        return None

    db_item = Rider(  
        name=Rider.name, 
        phone_number=Rider.phone_number, 
        status=Rider.status, 
        license=Rider.license, 
        rating=Rider.rating, 
        vehicle_type=Rider.vehicle_type

    )

    db = next(get_db())
    try:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return get_one(db_item.name)  

    except exc.IntegrityError:
        db.rollback()  
        raise Duplicate(msg=f"Rider (name: {Rider.name}) already exists")

def modify(rider_id: str, rider: RiderBase ) -> RiderBase :
    if not (rider_id and rider):
        return None

    db = next(get_db())
    item = db.query(Rider).filter(Rider.id == int(rider_id)).one_or_none()  

    if item:
        for var, value in vars(rider).items():
            if value is not None: 
                setattr(item, var, value)
        db.commit()
        db.refresh(item)
        return get_one(item.name) 
    else:
        raise Missing(msg=f"Rider (id: {rider_id}) not found")  

def delete(rider_id: str) -> bool:
    if not rider_id:
        return False

    db = next(get_db())
    item = db.query(Rider).filter(Rider.id == int(rider_id)).one_or_none() 
    if item:
        db.delete(item)
        db.commit()
        return True
    else:
        return False  
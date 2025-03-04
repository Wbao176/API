from src.data.schemas import RiderBase
import src.data.rider as data
from math import radians, sin, cos, sqrt, atan2
def get_all() -> list[RiderBase]:
    return data.get_all()

def get_one(name: str) -> RiderBase | None:
    return data.get_one(name)

def create(rider: RiderBase) -> RiderBase:
    return data.create(rider)

def replace(rider: RiderBase) -> RiderBase:
    return data.modify(rider)

def modify(rider: RiderBase) -> RiderBase:
    return data.modify(rider)


def delete(rider_id: str) -> bool:
    return data.delete(rider_id)

def calculate_distance(lat1, lon1, lat2, lon2):   
    R = 6371  
    phi1 = radians(lat1)
    phi2 = radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)

    #trich refe
    a = sin(dphi/2)**2 + cos(phi1) * cos(phi2) * sin(dlambda/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    return R * c 


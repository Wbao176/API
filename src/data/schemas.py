from pydantic import BaseModel
class RiderBase(BaseModel):
    name: str
    phone_number: str
    status: bool
    license: str
    rating: int
    vehicle_type:str
    latitude: float
    longitude: float
class RiderCreate(RiderBase):
    pass

class Rider(RiderBase):
    id: int

class UserInput(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    is_a_rider: bool
    hash: str  

class UserOutput(BaseModel):
    username: str

class User(UserOutput):
    id: int

class Config:
    from_attributes = True
from sqlalchemy import Column, Integer, String, Boolean  # Use Boolean instead of bool
from src.data.init import Base  

class Rider(Base):
    __tablename__ = "rider"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String, index=True)  # Corrected typo here
    status = Column(Boolean, index=True)  # Use Boolean instead of bool
    license = Column(String, index=True)
    rating = Column(Integer, index=True)
    vehicle_type = Column(String, index=True)

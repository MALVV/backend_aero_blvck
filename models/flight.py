from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.place import PlaceModel
Base = declarative_base()

class FlightModel(Base):
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String(50))
    origin_id = Column(Integer,ForeignKey(PlaceModel.id))
    destination_id = Column(Integer,ForeignKey(PlaceModel.id))
    departure_date = Column(String(10))
    departure_time = Column(String(10))
    
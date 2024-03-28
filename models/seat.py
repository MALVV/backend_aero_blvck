from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


from models.flight import FlightModel

Base = declarative_base()

class SeatModel(Base):
    __tablename__ = 'seat'
    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(Integer, ForeignKey(FlightModel.id))
    ##flight_id = Column(Integer, ForeignKey('flight.id')
    seat_number = Column(String(50))
    passenger_name = Column(String(50))
    status_seat = Column(String(50))


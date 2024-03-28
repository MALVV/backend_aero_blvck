from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from typing import List
from sqlalchemy.orm import aliased

from schemas.flight import FlightCreate
from models.flight import FlightModel

from models.place import PlaceModel
from models.seat import SeatModel

class FlightService:

    @staticmethod
    def create_flight(db: Session, flight: FlightCreate):
        try:
            new_flight = FlightModel(flight_number=flight.flight_number, origin_id=flight.origin_id, destination_id=flight.destination_id, departure_date=flight.departure_date, departure_time=flight.departure_time)
            db.add(new_flight)
            db.commit()
            db.refresh(new_flight)
            return new_flight
        except SQLAlchemyError as e:
            db.rollback()
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
        
    @staticmethod
    def get_flights_data(db: Session):
        try:
            flights = db.query(FlightModel).all()

            return flights
        except SQLAlchemyError as e:
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
    
    @staticmethod
    def get_flight_by_id(db: Session, flight_id: int):
        try:
            flight = db.query(FlightModel).filter(FlightModel.id == flight_id).first()
            return flight
        except SQLAlchemyError as e:
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
        
    @staticmethod
    def get_seats_by_flight_id(db: Session, flight_id: int):
        try:
            seats = db.query(SeatModel).filter(SeatModel.flight_id == flight_id).all()
            return seats
        except SQLAlchemyError as e:
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
    @staticmethod
    def get_all_flights_full_data(db: Session):
        try:
            OriginPlace = aliased(PlaceModel)
            DestinationPlace = aliased(PlaceModel)

            flights = db.query(FlightModel.id, OriginPlace.city.label("origin_city"), 
                            DestinationPlace.city.label("destination_city"),
                            FlightModel.departure_date, FlightModel.departure_time) \
                        .join(OriginPlace, FlightModel.origin_id == OriginPlace.id) \
                        .join(DestinationPlace, FlightModel.destination_id == DestinationPlace.id) \
                        .all()
            
            formatted_flights = []
            for id, origin_city, destination_city, departure_date, departure_time in flights:
                formatted_flight = {
                    "id": id,
                    "origin_city": origin_city,
                    "destination_city": destination_city,
                    "departure_date": departure_date,
                    "departure_time": departure_time
                }
                formatted_flights.append(formatted_flight)
            
            return formatted_flights
        except SQLAlchemyError as e:
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
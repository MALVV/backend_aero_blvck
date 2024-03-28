from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from typing import List

from schemas.seat import SeatCreate
from models.seat import SeatModel

class SeatService:

    @staticmethod
    def create_seat(db: Session, seat: SeatCreate):
        try:
            new_seat = SeatModel(seat_number=seat.seat_number, passenger_name=seat.passenger_name, status_seat=seat.status_seat,flight_id=seat.flight_id)
            db.add(new_seat)
            db.commit()
            db.refresh(new_seat)
            return new_seat
        except SQLAlchemyError as e:
            db.rollback()
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
        
    @staticmethod
    def get_seats(db: Session):
        try:
            seats = db.query(SeatModel).all()
            return seats
        except SQLAlchemyError as e:
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
        
    @staticmethod
    def get_seat_by_id(db: Session, seat_id: int):
        try:
            seat = db.query(SeatModel).filter(SeatModel.id == seat_id).first()
            return seat
        except SQLAlchemyError as e:
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
    
    @staticmethod
    def get_seat_by_number(db: Session, seat_number: str):
        try:
            seat = db.query(SeatModel).filter(SeatModel.seat_number == seat_number).first()
            return seat
        except SQLAlchemyError as e:
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
    
    @staticmethod
    def get_seats_by_status(db: Session, status: str):
        try:
            seats = db.query(SeatModel).filter(SeatModel.status_seat == status).all()
            return seats
        except SQLAlchemyError as e:
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
        
    @staticmethod
    def update_seat_status(db: Session, seat_id: int, status: str):
        try:
            seat = db.query(SeatModel).filter(SeatModel.id == seat_id).first()
            seat.status_seat = status
            db.commit()
            db.refresh(seat)
            return seat
        except SQLAlchemyError as e:
            db.rollback()
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
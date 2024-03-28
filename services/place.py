from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from typing import List

from schemas.place import PlaceCreate
from models.place import PlaceModel

class PlaceService:

    @staticmethod
    def create_place(db: Session, place: PlaceCreate):
        try:
            new_place = PlaceModel(city=place.city, country=place.country)
            db.add(new_place)
            db.commit()
            db.refresh(new_place)
            return new_place
        except SQLAlchemyError as e:
            db.rollback()
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
    
    @staticmethod
    def get_places(db: Session):
        try:
            places = db.query(PlaceModel).all()
            return places
        except SQLAlchemyError as e:
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
        
    @staticmethod
    def get_place_by_id(db: Session, place_id: int):
        try:
            place = db.query(PlaceModel).filter(PlaceModel.id == place_id).first()
            return place
        except SQLAlchemyError as e:
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
    
    @staticmethod
    def get_place_by_city(db: Session, city: str):
        try:
            place = db.query(PlaceModel).filter(PlaceModel.city == city).first()
            return place
        except SQLAlchemyError as e:
            error_message = f"Database error: {e.orig}"
            raise HTTPException(status_code=500, detail=error_message)
from fastapi import FastAPI,APIRouter, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Annotated
from services.db import get_db

from schemas.seat import SeatCreate
from services.seat import SeatService

seat_router = APIRouter()

@seat_router.get("/",status_code=status.HTTP_200_OK)
def get_seats(db: Session=  Depends(get_db)):
    return SeatService.get_seats(db)

@seat_router.get("/{seat_id}",status_code=status.HTTP_200_OK)
def get_seat_by_id(seat_id: int, db: Session=  Depends(get_db)):
    return SeatService.get_seat_by_id(db, seat_id)

@seat_router.post("/",status_code=status.HTTP_201_CREATED)
def create_seat(seat: SeatCreate, db: Session= Depends(get_db)):
    return SeatService.create_seat(db, seat)

@seat_router.get("/number/{seat_number}",status_code=status.HTTP_200_OK)
def get_seat_by_number(seat_number: str, db: Session=  Depends(get_db)):
    return SeatService.get_seat_by_number(db, seat_number)

@seat_router.get("/status/{status}",status_code=status.HTTP_200_OK)
def get_seats_by_status(status_seat: str, db: Session=  Depends(get_db)):
    return SeatService.get_seats_by_status(db, status_seat)



@seat_router.put("/{seat_id}",status_code=status.HTTP_200_OK)
def update_seat_status(seat_id: int, status_seat: str, db: Session=  Depends(get_db)):
    return SeatService.update_seat_status(db, seat_id, status_seat)
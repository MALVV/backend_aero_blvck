from fastapi import FastAPI,APIRouter, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Annotated
from services.db import get_db

from schemas.flight import FlightCreate
from services.flight import FlightService

flight_router = APIRouter()

@flight_router.get("/",status_code=status.HTTP_200_OK)
def get_flights(db: Session=  Depends(get_db)):
    return FlightService.get_flights_data(db)

@flight_router.get("/{flight_id}",status_code=status.HTTP_200_OK)
def get_flight_by_id(flight_id: int, db: Session=  Depends(get_db)):
    return FlightService.get_flight_by_id(db, flight_id)

@flight_router.post("/",status_code=status.HTTP_201_CREATED)
def create_flight(flight: FlightCreate, db: Session= Depends(get_db)):
    return FlightService.create_flight(db, flight)

@flight_router.get("/{flight_id}/seats",status_code=status.HTTP_200_OK)
def get_seats_by_flight_id(flight_id: int, db: Session=  Depends(get_db)):
    return FlightService.get_seats_by_flight_id(db, flight_id)

@flight_router.get("/full_info/",status_code=status.HTTP_200_OK)
def get_full_info_flights_places(db: Session=  Depends(get_db)):
    return FlightService.get_all_flights_full_data(db)




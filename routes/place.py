from fastapi import FastAPI,APIRouter, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Annotated
from services.db import get_db

from schemas.place import PlaceCreate
from services.place import PlaceService

place_router = APIRouter()

@place_router.get("/",status_code=status.HTTP_200_OK)
def get_places(db: Session=  Depends(get_db)):
    return PlaceService.get_places(db)

@place_router.get("/{place_id}",status_code=status.HTTP_200_OK)
def get_place_by_id(place_id: int, db: Session=  Depends(get_db)):
    return PlaceService.get_place_by_id(db, place_id)

@place_router.post("/",status_code=status.HTTP_201_CREATED)
def create_place(place: PlaceCreate, db: Session= Depends(get_db)):
    return PlaceService.create_place(db, place)

@place_router.get("/city/{city}",status_code=status.HTTP_200_OK)
def get_place_by_city(city: str, db: Session=  Depends(get_db)):
    return PlaceService.get_place_by_city(db, city)

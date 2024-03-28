from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated
from services.db import Base, SessionLocal, engine






app = FastAPI()

origins = [

    "http://localhost:3000",
    "http://127.0.0.1:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

#Place
from routes.place import place_router
from models.place import PlaceModel
PlaceModel.metadata.create_all(bind=engine)
app.include_router(place_router, prefix="/place", tags=["place"])

#Flight
from routes.flight import flight_router
from models.flight import FlightModel
FlightModel.metadata.create_all(bind=engine)
app.include_router(flight_router, prefix="/flight", tags=["flight"])

#Seat
from routes.seat import seat_router
from models.seat import SeatModel
SeatModel.metadata.create_all(bind=engine)
app.include_router(seat_router, prefix="/seat", tags=["seat"])



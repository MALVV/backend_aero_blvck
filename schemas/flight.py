from pydantic import BaseModel

class FlightCreate(BaseModel):
    flight_number: str
    origin_id: int
    destination_id: int
    departure_date: str
    departure_time: str
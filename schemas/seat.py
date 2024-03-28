from pydantic import BaseModel

class SeatCreate(BaseModel):
    seat_number: str
    flight_id: int
    passenger_name: str
    status_seat: str


from pydantic import BaseModel

class PlaceCreate(BaseModel):
    city: str
    country: str
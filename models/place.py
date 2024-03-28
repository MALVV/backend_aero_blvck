from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PlaceModel(Base):
    __tablename__ = 'place'
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(50))
    country = Column(String(50))
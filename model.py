from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from pydantic import BaseModel
from db import Base


class PatientTable(Base):
    __tablename__ = 'patient'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(225), nullable=False)
    last_name = Column(String(225), nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.utcnow)


class Patient(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth: datetime
    created: datetime

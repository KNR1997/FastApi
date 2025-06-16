from sqlalchemy import Column, Integer, String
from db.base import Base
from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

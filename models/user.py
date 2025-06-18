from sqlalchemy import Column, Integer, String
from db.base import Base

class User(Base):
    __tablename__ = "ousr"

    id = Column(Integer, primary_key=True)
    user_id = Column(String(100))
    user_name = Column(String(100))

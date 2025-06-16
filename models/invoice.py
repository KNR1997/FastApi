from sqlalchemy import Column, Integer, String
from db.base import Base
from pydantic import BaseModel

class Invoice(Base):
    __tablename__ = "invoice"

    id = Column(Integer, primary_key=True)
    invoice_number = Column(String(100))
    company_name = Column(String(100))
    value = Column(String(50))
    created_at = Column(String(50))

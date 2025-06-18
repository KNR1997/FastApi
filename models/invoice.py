from sqlalchemy import Column, Integer, String, Enum as SqlEnum
from db.base import Base

class Invoice(Base):
    __tablename__ = "invoice"

    id = Column(Integer, primary_key=True)
    invoice_number = Column(String(100))
    company_name = Column(String(100))
    finance_status = Column(String(100))
    fgs_status = Column(String(100))
    value = Column(String(50))
    created_at = Column(String(50))
    created_user = Column(String(50))

from sqlalchemy import Column, Integer, String
from db.base import Base

class InvoiceMiddlware(Base):
    __tablename__ = "oinv"

    id = Column(Integer, primary_key=True)
    docnumber = Column(String(100))
    docdate = Column(String(100))
    cardcode = Column(String(50))
    doctotal = Column(String(50))
    u_wareh = Column(String(50))
    usersign = Column(String(50))
    exmple = Column(String(50))

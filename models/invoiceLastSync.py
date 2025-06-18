from sqlalchemy import Column, Integer
from db.base import Base

class InvoiceLastSync(Base):
    __tablename__ = "invoice_last_sync"

    id = Column(Integer, primary_key=True)
    last_synced_invoice_id = Column(Integer)

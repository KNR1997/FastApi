import asyncio
from fastapi_utilities import repeat_every, repeat_at

from db.external_db1 import ExternalSession1
from db.primary_db import PrimarySession
from models.invoice import Invoice
from models.invoiceMiddleware import InvoiceMiddlware
from models.invoiceLastSync import InvoiceLastSync
from enums import EStatus

@repeat_every(seconds=5)
async def load_data():
    print("Load data")


@repeat_at(cron="* * * * *")
def test_cron_job():
    print("cron job executed")


@repeat_at(cron="* * * * *")
def sync_invoices():
    ext_session = ExternalSession1()
    primary_session = PrimarySession()

    try:
        # Step 1: Get last synced invoice id from the local DB
        last_sync = primary_session.query(InvoiceLastSync).first()
        last_synced_id = last_sync.last_synced_invoice_id if last_sync else 0

        print('last_synced_id: ', last_synced_id)

        # Step 2: Fetch new invoices from external DB
        invoices = ext_session.query(InvoiceMiddlware).filter(InvoiceMiddlware.id > last_synced_id).order_by(InvoiceMiddlware.id.asc()).all()
        print(f"Fetched {len(invoices)} new invoices from external db1")

        # Step 3: Sync to primary DB
        max_id = last_synced_id
        for invoice in invoices:
            # Add to your main DB (you can upsert if needed)
            primary_session.add(Invoice(
                id=invoice.id,
                invoice_number=invoice.docnumber,
                company_name=invoice.u_wareh,
                finance_status=EStatus.PENDING,
                fgs_status=EStatus.PENDING,
                value=invoice.doctotal,
                created_at=invoice.docdate,
            ))
            max_id = max(max_id, invoice.id)

        # Step 4: Update sync marker
        if last_sync:
            last_sync.last_synced_invoice_id = max_id
        else:
            new_marker = InvoiceLastSync(id=1, last_synced_invoice_id=max_id)
            primary_session.add(new_marker)

        primary_session.commit()
        print("Sync complete.")
    except Exception as e:
        print("Error during sync:", e)
        primary_session.rollback()
    finally:
        ext_session.close()
        primary_session.close()

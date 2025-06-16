from db.external_db1 import ExternalSession1
from db.primary_db import PrimarySession
from models.invoice import Invoice


def sync_invoices_from_external():
    ext_session = ExternalSession1()
    primary_session = PrimarySession()

    try:
        invoices = ext_session.query(Invoice).all()
        print(f"Fetched {len(invoices)} invoices from external db1")

        for invoice in invoices:
            existing = primary_session.query(Invoice).filter_by(id=invoice.id).first()
            if existing:
                existing.value = invoice.value
            else:
                primary_session.add(Invoice(id=invoice.id,
                                            invoice_number=invoice.invoice_number,
                                            company_name=invoice.company_name,
                                            value=invoice.value,
                                            created_at=invoice.created_at,
                                            ))

        primary_session.commit()
        print("Sync complete.")
    except Exception as e:
        print("Error during sync:", e)
        primary_session.rollback()
    finally:
        ext_session.close()
        primary_session.close()

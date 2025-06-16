from fastapi import FastAPI

from services.sync import sync_invoices_from_external

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sync")
def trigger_sync():
    sync_invoices_from_external()
    return {"status": "sync complete"}

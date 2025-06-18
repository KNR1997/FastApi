from fastapi import FastAPI
from typing import Union
from contextlib import asynccontextmanager

from events import load_data,test_cron_job, sync_invoices
from services.sync import sync_invoices_from_external


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await load_data()
    # test_cron_job()
    sync_invoices()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/sync")
def trigger_sync():
    sync_invoices_from_external()
    return {"status": "sync complete"}

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

EXTERNAL_DB1_URL = os.getenv("EXTERNAL_DB1_URL")
external_engine1 = create_engine(EXTERNAL_DB1_URL)
ExternalSession1 = sessionmaker(bind=external_engine1)

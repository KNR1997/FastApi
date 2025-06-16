import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

PRIMARY_DB_URL = os.getenv("PRIMARY_DB_URL")
primary_engine = create_engine(PRIMARY_DB_URL)
PrimarySession = sessionmaker(bind=primary_engine)

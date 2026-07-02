import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent

FILE_PATH = BASE_DIR / "data" / "nyc-311-etl-request.csv"
SCHEMA_PATH = BASE_DIR / "schema.sql"

DATABASE_NAME = os.getenv("DATABASE_NAME", "nyc_311.db")
DB_PATH = BASE_DIR / "output" / DATABASE_NAME

SAMPLE_SIZE = int(os.getenv("SAMPLE_SIZE", 5000))
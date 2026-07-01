
import sqlite3
import pandas as pd
from pathlib import Path
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "data" / "nyc-311-etl-request.csv"
DB_PATH = BASE_DIR / "output" / "nyc_311.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"

print("=" * 60)
print("NYC 311 ETL Pipeline")
print("=" * 60)

# Extract
df = extract_data(FILE_PATH)

# Transform
df = transform_data(df)

# Load
load_data(df, DB_PATH, SCHEMA_PATH)
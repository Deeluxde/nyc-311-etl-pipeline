
import sqlite3
import pandas as pd
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from config import FILE_PATH, DB_PATH, SCHEMA_PATH

print("=" * 60)
print("NYC 311 ETL Pipeline")
print("=" * 60)

# Extract
df = extract_data(FILE_PATH)

# Transform
df = transform_data(df)

# Load
load_data(df, DB_PATH, SCHEMA_PATH)
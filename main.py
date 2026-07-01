import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "data" / "nyc-311-etl-request.csv"
DB_PATH = BASE_DIR / "output" / "nyc_311.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"

print("=" * 60)
print("NYC 311 ETL Pipeline")
print("=" * 60)

# Extract
df = pd.read_csv(FILE_PATH, nrows=5000)
print(f"Rows extracted: {len(df)}")

# Transform
df = df.drop_duplicates()

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)

for col in df.select_dtypes(include="object"):
    df[col] = df[col].astype(str).str.strip()

df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")
df["closed_date"] = pd.to_datetime(df["closed_date"], errors="coerce")

# Keep only columns needed for SQLite table
df = df[
    [
        "unique_key",
        "created_date",
        "closed_date",
        "agency",
        "agency_name",
        "problem_formerly_complaint_type",
        "problem_detail_formerly_descriptor",
        "location_type",
        "incident_zip",
        "incident_address",
        "street_name",
        "city",
        "borough",
        "status",
        "open_data_channel_type",
        "latitude",
        "longitude",
    ]
]

df = df.rename(
    columns={
        "problem_formerly_complaint_type": "complaint_type",
        "problem_detail_formerly_descriptor": "complaint_detail",
    }
)

print(f"Rows after cleaning: {len(df)}")

# Load
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
conn = sqlite3.connect(DB_PATH)

with open(SCHEMA_PATH, "r") as f:
    conn.executescript(f.read())

df.to_sql("service_requests", conn, if_exists="append", index=False)

row_count = pd.read_sql_query(
    "SELECT COUNT(*) AS total_rows FROM service_requests",
    conn
)

print("\nSQLite database created successfully!")
print(row_count)

conn.close()
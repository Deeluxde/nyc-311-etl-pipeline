from pathlib import Path

BASE_DIR = Path(__file__).parent

FILE_PATH = BASE_DIR / "data" / "nyc-311-etl-request.csv"
DB_PATH = BASE_DIR / "output" / "nyc_311.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"

SAMPLE_SIZE = 5000
from config import FILE_PATH, DB_PATH, SCHEMA_PATH
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from src.validate import validate_data

def main():
    print("=" * 60)
    print("NYC 311 ETL Pipeline")
    print("=" * 60)

    # Extract
    df = extract_data(FILE_PATH)

    # Transform
    df = transform_data(df)

    # Validate
    df = validate_data(df)

    # Load
    load_data(df, DB_PATH, SCHEMA_PATH)


if __name__ == "__main__":
    main()
import sqlite3
import pandas as pd
from src.logger import get_logger

logger = get_logger(__name__)


def load_data(df, db_path, schema_path):
    """
    Load transformed data into SQLite.
    """

    logger.info("Starting data load")

    db_path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_path)

    with open(schema_path, "r") as f:
        conn.executescript(f.read())

    df.to_sql(
        "service_requests",
        conn,
        if_exists="append",
        index=False
    )

    row_count = pd.read_sql_query(
        """
        SELECT COUNT(*) AS total_rows
        FROM service_requests
        """,
        conn,
    )

    logger.info("SQLite database created successfully")
    logger.info(f"Total rows loaded: {row_count.iloc[0]['total_rows']}")

    print(row_count)

    conn.close()

    logger.info("Database connection closed")
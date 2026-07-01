import sqlite3
import pandas as pd


def load_data(df, db_path, schema_path):
    """
    Load transformed data into SQLite.
    """

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

    print("\nSQLite database created successfully!")
    print(row_count)

    conn.close()
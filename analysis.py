import sqlite3
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from config import DB_PATH


OUTPUT_DIR = Path("analysis")
OUTPUT_DIR.mkdir(exist_ok=True)


def run_query(conn, query):
    """
    Run a SQL query and return the result as a pandas DataFrame.
    """
    return pd.read_sql_query(query, conn)


def main():
    """
    Run analytical queries against the SQLite database.
    """

    conn = sqlite3.connect(DB_PATH)

    print("\nNYC 311 Analysis")
    print("=" * 60)

    # Question 1
    print("\nQuestion 1: Which complaint types occur most frequently?")
    print("Rationale: This helps identify the most common service issues reported by residents.\n")

    top_complaints_sql = """
    SELECT
        complaint_type,
        COUNT(*) AS total_requests
    FROM service_requests
    GROUP BY complaint_type
    ORDER BY total_requests DESC
    LIMIT 10;
    """

    top_complaints = run_query(conn, top_complaints_sql)
    print(top_complaints)

    # Question 2
    print("\nQuestion 2: Which borough has the highest number of service requests?")
    print("Rationale: This helps compare demand for city services across boroughs.\n")

    borough_sql = """
    SELECT
        borough,
        COUNT(*) AS total_requests
    FROM service_requests
    GROUP BY borough
    ORDER BY total_requests DESC;
    """

    borough_results = run_query(conn, borough_sql)
    print(borough_results)

    # Question 3
    print("\nQuestion 3: Which agencies receive the most service requests?")
    print("Rationale: This helps understand which city agencies handle the highest service volume.\n")

    agency_sql = """
    SELECT
        agency,
        COUNT(*) AS total_requests
    FROM service_requests
    GROUP BY agency
    ORDER BY total_requests DESC
    LIMIT 10;
    """

    agency_results = run_query(conn, agency_sql)
    print(agency_results)

    # Question 4 - Python chart
    print("\nQuestion 4: Visualizing the top complaint types using Python")
    print("Rationale: A bar chart makes it easier to compare high-volume complaint categories.\n")

    plt.figure(figsize=(10, 6))
    plt.bar(top_complaints["complaint_type"], top_complaints["total_requests"])
    plt.xlabel("Complaint Type")
    plt.ylabel("Total Requests")
    plt.title("Top 10 NYC 311 Complaint Types")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    chart_path = OUTPUT_DIR / "top_complaint_types.png"
    plt.savefig(chart_path)

    print(f"\nChart saved to: {chart_path}")

    conn.close()


if __name__ == "__main__":
    main()
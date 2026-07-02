import pandas as pd
from src.logger import get_logger


logger = get_logger(__name__)


def extract_data(file_path):
    """
    Extract data from the CSV file.
    """

    logger.info("Starting data extraction")

    df = pd.read_csv(file_path, nrows=5000)

    logger.info(f"Rows extracted: {len(df)}")

    return df
import pandas as pd

from config import SAMPLE_SIZE
from src.logger import get_logger

logger = get_logger(__name__)

def extract_data(file_path):
    """
    Extract NYC 311 data from a CSV file.
    """

    logger.info("Starting data extraction")

    try:
        df = pd.read_csv(
            file_path,
            nrows=SAMPLE_SIZE
        )

        logger.info(f"Rows extracted: {len(df):,}")

        return df

    except FileNotFoundError:
        logger.exception("CSV file not found.")
        raise

    except pd.errors.ParserError:
        logger.exception("Unable to parse CSV file.")
        raise

    except Exception:
        logger.exception("Unexpected error during extraction.")
        raise
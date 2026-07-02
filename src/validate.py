from src.logger import get_logger

logger = get_logger(__name__)


def validate_data(df):
    """
    Validate the transformed dataframe.
    """

    logger.info("Starting data validation")

    required_columns = [
        "unique_key",
        "created_date",
        "agency",
        "status"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    missing = df["unique_key"].isnull().sum()

    if missing > 0:
        logger.warning(f"{missing} records missing unique_key")

    logger.info("Validation completed successfully")

    return df
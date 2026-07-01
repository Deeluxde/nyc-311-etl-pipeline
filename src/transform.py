import pandas as pd

def transform_data(df):
    """
    Clean and transform NYC 311 data.
    """

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

    return df
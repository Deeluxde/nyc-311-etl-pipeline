import pandas as pd

def extract_data(file_path):
    """
    Extract data from the CSV file.
    """
    df = pd.read_csv(file_path, nrows=5000)
    print(f"Rows extracted: {len(df)}")
    return df
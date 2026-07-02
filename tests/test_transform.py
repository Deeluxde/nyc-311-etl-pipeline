import pandas as pd

from src.transform import transform_data


def test_transform_removes_duplicates():

    df = pd.DataFrame({
        "created_date": ["2026-01-01", "2026-01-01"],
        "closed_date": ["2026-01-02", "2026-01-02"],
        "agency": ["NYPD", "NYPD"],
        "agency_name": ["Police", "Police"],
        "problem_formerly_complaint_type": ["Noise", "Noise"],
        "problem_detail_formerly_descriptor": ["Loud Music", "Loud Music"],
        "location_type": ["Street", "Street"],
        "incident_zip": ["10001", "10001"],
        "incident_address": ["123 Main", "123 Main"],
        "street_name": ["Main", "Main"],
        "city": ["New York", "New York"],
        "borough": ["MANHATTAN", "MANHATTAN"],
        "status": ["Closed", "Closed"],
        "open_data_channel_type": ["PHONE", "PHONE"],
        "latitude": [40.0, 40.0],
        "longitude": [-73.0, -73.0],
        "unique_key": [1, 1]
    })

    cleaned = transform_data(df)

    assert len(cleaned) == 1
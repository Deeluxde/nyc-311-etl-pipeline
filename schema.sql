DROP TABLE IF EXISTS service_requests;

CREATE TABLE service_requests (
    unique_key INTEGER PRIMARY KEY,
    created_date TEXT,
    closed_date TEXT,
    agency TEXT,
    agency_name TEXT,
    complaint_type TEXT,
    complaint_detail TEXT,
    location_type TEXT,
    incident_zip TEXT,
    incident_address TEXT,
    street_name TEXT,
    city TEXT,
    borough TEXT,
    status TEXT,
    open_data_channel_type TEXT,
    latitude REAL,
    longitude REAL
);

CREATE INDEX idx_service_requests_created_date
ON service_requests(created_date);

CREATE INDEX idx_service_requests_borough
ON service_requests(borough);

CREATE INDEX idx_service_requests_complaint_type
ON service_requests(complaint_type);

CREATE INDEX idx_service_requests_status
ON service_requests(status);
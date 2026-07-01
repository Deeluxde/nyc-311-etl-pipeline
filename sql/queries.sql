-- Total records
SELECT COUNT(*) AS total_requests
FROM service_requests;

-- Top complaint types
SELECT complaint_type, COUNT(*) AS total_requests
FROM service_requests
GROUP BY complaint_type
ORDER BY total_requests DESC
LIMIT 10;

-- Requests by borough
SELECT borough, COUNT(*) AS total_requests
FROM service_requests
GROUP BY borough
ORDER BY total_requests DESC;

-- Requests by agency
SELECT agency, COUNT(*) AS total_requests
FROM service_requests
GROUP BY agency
ORDER BY total_requests DESC;

-- Requests by status
SELECT status, COUNT(*) AS total_requests
FROM service_requests
GROUP BY status
ORDER BY total_requests DESC;
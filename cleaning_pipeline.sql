-- cleaning_pipeline.sql
-- Sample SQL script to clean and prepare lead data

SELECT
  LOWER(TRIM(email)) AS normalized_email,
  UPPER(source) AS lead_source,
  CASE
    WHEN country IS NULL OR country = '' THEN 'Unknown'
    ELSE country
  END AS country_cleaned,
  created_at,
  campaign_id
FROM
  raw_leads
WHERE
  email IS NOT NULL
  AND created_at >= '2024-01-01';

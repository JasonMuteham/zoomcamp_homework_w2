CREATE SCHEMA IF NOT EXISTS raw;
CREATE OR REPLACE TABLE raw.green_taxi AS (SELECT * FROM {{ df_1 }} );
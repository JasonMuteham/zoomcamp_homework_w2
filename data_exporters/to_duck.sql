CREATE SCHEMA IF NOT EXISTS mage;
CREATE OR REPLACE TABLE mage.green_taxi AS (SELECT * FROM {{ df_1 }} );
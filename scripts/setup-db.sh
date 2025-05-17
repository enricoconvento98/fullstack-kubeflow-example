#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE IF NOT EXISTS pipeline_runs (
        run_id VARCHAR(50) PRIMARY KEY,
        pipeline_name VARCHAR(100),
        status VARCHAR(20),
        start_time TIMESTAMP,
        end_time TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS model_metrics (
        id SERIAL PRIMARY KEY,
        run_id VARCHAR(50) REFERENCES pipeline_runs(run_id),
        metric_name VARCHAR(50),
        metric_value FLOAT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
EOSQL
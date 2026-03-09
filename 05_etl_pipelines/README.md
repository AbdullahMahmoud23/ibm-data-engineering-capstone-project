# Module 5: ETL & Data Pipelines Orchestration

## Project Overview

This module demonstrates the core of Data Engineering: extracting data from an operational database, transforming it, loading it into a data warehouse, and orchestrating the entire workflow using Apache Airflow.

## Part 1: Python ETL Pipeline

I developed a Python-based ETL script to synchronize data between a transactional database and an analytical data warehouse.

- **Extraction:** Queried a MySQL database to identify and pull only incremental, newly inserted records (OLTP).
- **Transformation:** Aligned schema differences between the source data and the target warehouse.
- **Loading:** Bulk-inserted the incremental records into a PostgreSQL Data Warehouse (OLAP).
- **Key File:** `automation.py`

## Part 2: Apache Airflow Orchestration

I utilized Apache Airflow (running locally via Docker) to build a Directed Acyclic Graph (DAG) that automates a daily log-processing pipeline.

- **Task 1 (Extract):** Parsed a raw web server access log to extract specific IP addresses using Bash operators.
- **Task 2 (Transform):** Filtered out restricted IP addresses from the extracted dataset.
- **Task 3 (Load):** Archived the transformed data into a compressed `.tar` file for storage.
- **Key File:** `Airflow/dags/process_web_log.py`

## Proof of Execution

The `Airflow/airflow.png` screenshot demonstrates the successful execution of the `process_web_log` DAG within the Airflow Web UI.

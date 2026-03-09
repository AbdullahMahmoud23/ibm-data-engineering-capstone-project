# IBM Data Engineering Professional Certificate Capstone

## Project Overview

This repository contains the final capstone project for the IBM Data Engineering Professional Certificate. The project demonstrates the ability to design, build, and orchestrate an end-to-end data pipeline that extracts data from operational databases, transforms it, loads it into a data warehouse, and surfaces insights through a Business Intelligence dashboard.

## Architecture & Tech Stack

- **Operational Database (OLTP):** MySQL
- **Data Warehouse (OLAP):** PostgreSQL
- **ETL Processing:** Python (`mysql-connector-python`, `psycopg2`)
- **Pipeline Orchestration:** Apache Airflow (Dockerized)
- **Data Analytics & BI:** Google Looker Studio
- **Version Control:** Git & GitHub

## Repository Structure

- `01_database_design/`: Scripts for designing and configuring the operational database schemas.
- `02_nosql_systems/`: Configurations and queries for NoSQL document and column-family stores.
- `03_data_warehousing/`: Schema design and setup for the PostgreSQL analytical data warehouse.
- `04_analytics/`: Exports and visual representations of the Business Intelligence dashboards built in Looker Studio.
- `05_etl_pipelines/`: Python extraction/loading scripts and the Apache Airflow DAGs used to automate the workflow.

## Key Features & Achievements

- Designed a normalized relational database schema for transactional e-commerce data.
- Built a Python-based incremental ETL pipeline to synchronize new records from MySQL to PostgreSQL without duplicating data.
- Orchestrated a daily batch-processing workflow using Apache Airflow and Bash operators to extract, filter, and archive server log files.
- Developed an interactive BI dashboard visualizing quarterly sales trends and categorical revenue distribution.

## How to Run the Infrastructure

A `docker-compose.yml` file is provided in the root directory to easily spin up the MySQL and PostgreSQL database instances required for the ETL scripts.

```bash
docker compose up -d
```

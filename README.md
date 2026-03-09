# IBM Data Engineering Professional Certificate Capstone

## Project Overview

This repository contains the final capstone project for the 14-course IBM Data Engineering Professional Certificate. The project demonstrates the ability to design, build, and orchestrate an end-to-end data pipeline that extracts data from operational databases, transforms it, loads it into a data warehouse, and leverages big data technologies for machine learning forecasting.

## Architecture & Tech Stack

- **Operational Database (OLTP):** MySQL
- **NoSQL Document Store:** MongoDB
- **Data Warehouse (OLAP):** PostgreSQL
- **ETL Processing:** Python (`mysql-connector-python`, `psycopg2`)
- **Pipeline Orchestration:** Apache Airflow (Dockerized)
- **Big Data & MLOps:** Apache Spark, PySpark, Spark MLlib
- **Data Analytics & BI:** Google Looker Studio / Cognos BI
- **Version Control:** Git & GitHub

## Repository Structure

- **`01_database_design/`**: Scripts for designing and configuring the operational relational database schemas.
- **`02_nosql_systems/`**: Configurations, JSON imports, and aggregation queries for MongoDB document stores.
- **`03_data_warehousing/`**: Schema design, star schema implementation, and setup for the PostgreSQL analytical data warehouse.
- **`04_analytics/`**: Exports and visual representations of the Business Intelligence dashboards, including grouping sets and materialized views.
- **`05_etl_pipelines/`**: Python extraction/loading scripts and the Apache Airflow DAGs used to automate the daily web log processing workflow.
- **`06_big_data_spark/`**: PySpark notebooks and pre-trained Spark MLlib linear regression models used to analyze search trends and forecast future e-commerce sales.

## Key Features & Achievements

- Designed a normalized relational database schema for transactional e-commerce data and implemented NoSQL document collections.
- Built a Python-based incremental ETL pipeline to synchronize new records from MySQL to PostgreSQL without duplicating data.
- Orchestrated a daily batch-processing workflow using Apache Airflow and Bash operators to extract, filter, and archive server log files.
- Developed interactive BI dashboards visualizing quarterly sales trends and categorical revenue distribution.
- Leveraged Apache Spark to process large-scale datasets and utilized a pre-trained Machine Learning model to forecast sales metrics.

## How to Run the Infrastructure

A `docker-compose.yml` file is provided in the root directory to easily spin up the MySQL and PostgreSQL database instances required for the ETL scripts.

```bash
docker compose up -d
```

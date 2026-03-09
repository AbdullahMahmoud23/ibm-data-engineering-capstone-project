# Module 3: Data Warehouse Design and Implementation (PostgreSQL)

## Project Overview

In this module, I transitioned from operational data storage to analytical data modeling. I designed and implemented a **Star Schema** Data Warehouse for "SoftCart," an e-commerce platform, to enable efficient multi-dimensional analysis of sales performance across different timeframes, categories, and geographies.

## Data Sources

The sample data for this project was provided in CSV format. You can download the raw datasets used to populate the data warehouse here:

- [DimDate.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/data/DimDate.csv)
- [DimCategory.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCategory.csv)
- [DimCountry.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCountry.csv)
- [FactSales.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/FactSales.csv)

## Architectural Design: The Star Schema

Using the provided e-commerce sample data, I identified the central business process (Sales) and the surrounding descriptive attributes (Dimensions).

### 1. Fact Table

- **`softcartFactSales`**: Stores quantitative data (`price`) and foreign keys linking to all dimensions.

### 2. Dimension Tables

- **`softcartDimDate`**: Enables time-series analysis (Year, Month, Weekday).
- **`softcartDimCategory`**: Categorizes products (e.g., Movie, Ebook, Song).
- **`softcartDimItem`**: Contains specific product details.
- **`softcartDimCountry`**: Allows for geographical sales distribution analysis.

## Technical Tasks Executed

- **Data Modeling:** Utilized pgAdmin ERD tool to design relationships and enforce referential integrity.
- **Schema Deployment:** Developed DDL scripts to initialize the `staging` database environment.
- **ETL (Load):** Populated the warehouse using optimized PostgreSQL `COPY` utilities for bulk data ingestion from CSV sources.
- **Advanced Analytics:** Implemented complex OLAP queries to generate business insights:
  - **Grouping Sets:** For independent totals across different dimensions.
  - **Rollup:** For hierarchical subtotals (Year > Country).
  - **Cube:** For cross-tabulation of all possible combinations of dimensions.
  - **Materialized Views:** Created a summary table for total sales per country to optimize dashboard performance.

## How to Run the Scripts

1. Run `CREATE_SCRIPT.sql` to build the Star Schema.
2. Execute `LOAD_QUERY.sql` to ingest the CSV data into the respective tables.
3. Use `QUERY_For_Analytics.sql` to generate analytical reports.

---

_This module demonstrates proficiency in Dimensional Modeling, Star Schema architecture, and Advanced SQL for Business Intelligence._

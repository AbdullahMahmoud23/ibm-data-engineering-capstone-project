# Module 6: Big Data Analytics & Spark MLOps

## Project Overview

This module represents the final phase of the Data Engineering Capstone Project. It focuses on leveraging Apache Spark to process large-scale datasets, analyze e-commerce search logs, and utilize a pre-trained Machine Learning model to forecast future sales.

## Technologies Used

- **Data Processing Framework:** Apache Spark (PySpark)
- **Programming Language:** Python
- **Environment:** Jupyter Notebook
- **Machine Learning Library:** Spark MLlib
- **Underlying Runtime:** Java 11 (Optimized for Spark local compatibility)

## Repository Structure

- `Bigdata and Spark_Spark_MLOps_v3.ipynb`: The primary Jupyter Notebook containing the PySpark code for data exploration, transformations, and sales forecasting.
- `searchterms.csv`: The raw dataset containing e-commerce search logs.
- `sales_prediction.model/`: A pre-trained Spark MLlib Linear Regression model used for forecasting.
- `my_backup_model.tar.gz`: A compressed archive of the prediction model, demonstrating file management and extraction via terminal commands.

## Key Tasks & Achievements

1. **Data Loading & Exploration:** Initialized a local Spark Session and loaded raw CSV data into a structured Spark DataFrame using schema inference.
2. **Big Data Analytics:** Queried the DataFrame using PySpark data manipulation functions to identify the frequency of specific keywords (e.g., "gaming laptop") and aggregated the top 5 most popular search terms across the platform.
3. **MLOps & Forecasting:** Downloaded, extracted, and loaded a pre-trained Spark ML regression model. Utilized `VectorAssembler` to transform input features and successfully predicted e-commerce sales for the year 2023.

## How to Run Locally

To execute this notebook on a local Windows machine, ensure that your Spark environment is configured correctly:

1. Verify your Java installation is compatible with Spark (Java 8 or 11 is required; newer versions may cause Py4J connection resets).
2. Ensure `SPARK_HOME` and `HADOOP_HOME` (with `winutils.exe`) are properly set in your Windows environment variables.
3. Install the required Python packages (`pip install pyspark findspark`).
4. Launch Jupyter Notebook, open `Bigdata and Spark_Spark_MLOps_v3.ipynb`, and run the cells sequentially.

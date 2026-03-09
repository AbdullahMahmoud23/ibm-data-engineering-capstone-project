# Module 2: NoSQL Data Management (MongoDB)

## Project Overview

This section of the Capstone project focuses on managing **unstructured and semi-structured data**. While the transactional sales data is stored in a relational MySQL database, the product catalog contains diverse items with varying attributes, making a NoSQL document store the superior choice.

## Why MongoDB?

For this specific catalog, **MongoDB** was selected for the following technical reasons:

- **Schema Flexibility:** Electronic products (laptops, smartphones, cameras) do not share the same attributes. MongoDB's BSON format allows us to store these different "shapes" in a single collection without managing complex SQL joins or null columns.
- **Scalability:** As the product catalog grows to millions of items, MongoDB’s horizontal scaling (sharding) capabilities ensure the platform remains performant.
- **Performance:** By indexing the `type` field, we achieved near-instant lookup times for category-based filtering, which is critical for an e-commerce storefront.

## Key Tasks Performed

1.  **Data Ingestion:** Automated the import of `catalog.json` into the `electronics` collection.
2.  **Indexing:** Created an ascending index on the `type` field to optimize search queries.
3.  **Data Aggregation:** Leveraged the MongoDB Aggregation Framework to calculate business metrics, such as the average screen size for mobile devices.
4.  **Data Export:** Developed an ETL procedure using `mongoexport` to transition specific catalog subsets into CSV format for downstream analytics.

## Files in this Directory

- `catalog.json`: Raw source data for the product catalog.
- `electronics.csv`: Exported dataset containing `_id`, `type`, and `model`.
- `terminal_commands.txt`:
  - Automation script to initialize the database and indexes.
  - Utility script to export data from MongoDB to CSV.
  - A collection of the aggregation and find queries used for analysis.

---

_This module demonstrates the ability to handle the "Variety" aspect of Big Data within a modern data engineering pipeline._

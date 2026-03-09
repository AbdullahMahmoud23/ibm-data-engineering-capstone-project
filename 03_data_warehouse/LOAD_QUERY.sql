-------- DimDate --------
-- Load the data
copy "DimDate" FROM 'A:\Projects\ibm-data-engineering-capstone-project\03_data_warehouse\DimDate.csv' DELIMITER ',' CSV HEADER;

-- Display the first 5 rows
SELECT * FROM "DimDate" LIMIT 5;

-------- DimCategory --------
-- Load the data
copy "DimCategory" FROM 'A:\Projects\ibm-data-engineering-capstone-project\03_data_warehouse\DimCategory.csv' DELIMITER ',' CSV HEADER;

-- Display the first 5 rows
SELECT * FROM "DimCategory" LIMIT 5;

-------- DimCountry --------
-- Load the data
copy "DimCountry" FROM 'A:\Projects\ibm-data-engineering-capstone-project\03_data_warehouse\DimCountry.csv' DELIMITER ',' CSV HEADER;

-- Display the first 5 rows
SELECT * FROM "DimCountry" LIMIT 5;

-------- FactSales --------
-- Load the data
copy "FactSales" FROM 'A:\Projects\ibm-data-engineering-capstone-project\03_data_warehouse\FactSales.csv' DELIMITER ',' CSV HEADER;

-- Display the first 5 rows
SELECT * FROM "FactSales" LIMIT 5;



-- Grouping Sets Query

SELECT 
    c.country AS country, 
    cat.category AS category, 
    SUM(f.amount) AS totalsales
FROM "FactSales" f
JOIN "DimCountry" c ON f.countryid = c.countryid
JOIN "DimCategory" cat ON f.categoryid = cat.categoryid
GROUP BY GROUPING SETS (c.country, cat.category);

-- Rollup Query

SELECT 
    d.year, 
    c.country, 
    SUM(f.amount) AS totalsales
FROM "FactSales" f
JOIN "DimDate" d ON f.dateid = d.dateid
JOIN "DimCountry" c ON f.countryid = c.countryid
GROUP BY ROLLUP (d.year, c.country)
ORDER BY d.year, c.country;

-- Cube Query

SELECT 
    d.year, 
    c.country, 
    AVG(f.amount) AS average_sales
FROM "FactSales" f
JOIN "DimDate" d ON f.dateid = d.dateid
JOIN "DimCountry" c ON f.countryid = c.countryid
GROUP BY CUBE (d.year, c.country)
ORDER BY d.year, c.country;

-- Create an MQT (Materialized Query Table)

CREATE MATERIALIZED VIEW total_sales_per_country AS
SELECT 
    c.country, 
    SUM(f.amount) AS total_sales
FROM "FactSales" f
JOIN "DimCountry" c ON f.countryid = c.countryid
GROUP BY c.country;

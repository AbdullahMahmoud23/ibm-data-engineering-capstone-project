CREATE TABLE IF NOT EXISTS sales_data (
    rowid INT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    price DECIMAL DEFAULT 0.0 NOT NULL,
    quantity INT,
    timeestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

SELECT * FROM sales_data LIMIT 10;
CREATE DATABASE IF NOT EXISTS sales_analysis;
USE sales_analysis;

CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    order_date DATE,
    region VARCHAR(50),
    category VARCHAR(100),
    product VARCHAR(100),
    quantity INT,
    unit_price DECIMAL(10,2),
    sales DECIMAL(12,2)
);

-- Import the cleaned CSV into the sales table.

-- Total revenue
SELECT ROUND(SUM(sales),2) AS total_revenue FROM sales;

-- Revenue by region
SELECT region, ROUND(SUM(sales),2) AS revenue
FROM sales GROUP BY region ORDER BY revenue DESC;

-- Revenue by category
SELECT category, ROUND(SUM(sales),2) AS revenue
FROM sales GROUP BY category ORDER BY revenue DESC;

-- Top 5 products
SELECT product, ROUND(SUM(sales),2) AS revenue
FROM sales GROUP BY product ORDER BY revenue DESC LIMIT 5;

-- Monthly revenue
SELECT DATE_FORMAT(order_date,'%Y-%m') AS month,
       ROUND(SUM(sales),2) AS revenue
FROM sales
GROUP BY DATE_FORMAT(order_date,'%Y-%m')
ORDER BY month;

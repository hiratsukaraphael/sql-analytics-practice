
-- ============================================================
-- SQL PORTFOLIO: JOIN FANOUT AND DATA ACCURACY
-- ============================================================
-- Topic: INNER JOIN, COUNT, DISTINCT, SUM, GROUP BY, HAVING
--
-- Business scenario:
-- An e-commerce company wants to calculate the number
-- of orders, total revenue, and items purchased per customer.
--
-- Main lesson:
-- Joining orders to order_items can duplicate order totals
-- because one order may contain multiple items.
-- ============================================================


-- ============================================================
-- 1. CREATE TABLES
-- ============================================================

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_total DECIMAL(10,2)
);

CREATE TABLE order_items (
    order_id INT,
    item_id INT PRIMARY KEY
);


-- ============================================================
-- 2. INSERT SAMPLE DATA
-- ============================================================

INSERT INTO orders (order_id, customer_id, order_total)
VALUES
    (1, 101, 40),
    (2, 101, 30),
    (3, 102, 50),
    (4, 103, 20),
    (5, 103, 60);

INSERT INTO order_items (order_id, item_id)
VALUES
    (1, 1001),
    (1, 1002),
    (2, 1003),
    (3, 1004),
    (3, 1005),
    (3, 1006),
    (4, 1007),
    (5, 1008),
    (5, 1009);


-- ============================================================
-- 3. VERIFY THE TABLES
-- ============================================================

SELECT * FROM orders;

SELECT * FROM order_items;


-- ============================================================
-- 4. UNDERSTANDING INNER JOIN
-- ============================================================
-- Each order appears once for every matching item.
-- For example, order 3 contains 3 items, so its
-- order_total of 50 appears three times.

SELECT
    o.order_id,
    o.customer_id,
    o.order_total,
    i.item_id
FROM orders o
INNER JOIN order_items i
    ON o.order_id = i.order_id;


-- ============================================================
-- 5. TASK A: COUNT DISTINCT ORDERS PER CUSTOMER
-- ============================================================
-- COUNT(DISTINCT) prevents the same order from being
-- counted multiple times after joining to order_items.

SELECT
    o.customer_id,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM orders o
INNER JOIN order_items i
    ON o.order_id = i.order_id
GROUP BY o.customer_id;


-- ============================================================
-- 6. TASK B: CALCULATE REVENUE PER CUSTOMER
-- ============================================================
-- The orders table already contains the information
-- required for this calculation.
--
-- No JOIN is needed.

SELECT
    customer_id,
    SUM(order_total) AS total_revenue
FROM orders
GROUP BY customer_id;


-- ============================================================
-- 7. TASK C: INCORRECT QUERY - JOIN FANOUT
-- ============================================================
-- WARNING: This query produces incorrect metrics.
--
-- COUNT(*) counts joined rows, not unique orders.
-- SUM(order_total) adds repeated order totals.

SELECT
    o.customer_id,
    COUNT(*) AS total_orders,
    SUM(o.order_total) AS total_revenue
FROM orders o
INNER JOIN order_items i
    ON o.order_id = i.order_id
GROUP BY o.customer_id;


-- ============================================================
-- 8. CORRECTED QUERY: ORDERS AND REVENUE
-- ============================================================
-- One row in orders represents one order.
-- Therefore, both metrics can be calculated directly.

SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    SUM(order_total) AS total_revenue
FROM orders
GROUP BY customer_id;


-- ============================================================
-- 9. COMPARE COUNT(*) WITH COUNT(DISTINCT)
-- ============================================================
-- Demonstrates how JOIN fanout changes row counts.

SELECT
    o.customer_id,
    COUNT(*) AS joined_rows,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM orders o
INNER JOIN order_items i
    ON o.order_id = i.order_id
GROUP BY o.customer_id;


-- ============================================================
-- 10. WHY SUM(DISTINCT) IS NOT A GENERAL SOLUTION
-- ============================================================
-- Two legitimate orders may have identical values.
-- SUM(DISTINCT order_total) would count that value once.
--
-- Example:
-- Order 1 = 50
-- Order 2 = 50
-- Order 3 = 30
--
-- SUM(DISTINCT order_total) = 80
-- Correct revenue = 130


-- ============================================================
-- 11. INTERVIEW QUESTION: WHERE VS HAVING
-- ============================================================
-- Find customers with more than two orders.
--
-- HAVING filters aggregated groups.
-- WHERE filters individual rows before aggregation.

SELECT
    customer_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 2;

-- Expected result: No rows.
-- No customer in this dataset has more than two orders.


-- ============================================================
-- 12. HAVING WITH TWO OR MORE ORDERS
-- ============================================================

SELECT
    customer_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) >= 2;

-- Expected result:
-- customer_id | total_orders
-- 101         | 2
-- 103         | 2


-- ============================================================
-- 13. FINAL BUSINESS REPORT
-- ============================================================
-- Correct customer-level order and revenue summary.

SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    SUM(order_total) AS total_revenue
FROM orders
GROUP BY customer_id
ORDER BY total_revenue DESC;


-- ============================================================
-- KEY TAKEAWAYS
-- ============================================================
-- 1. Always identify what one row represents.
-- 2. One-to-many JOINs can multiply rows.
-- 3. COUNT(DISTINCT order_id) counts unique orders.
-- 4. SUM(order_total) can inflate revenue after a JOIN.
-- 5. SUM(DISTINCT order_total) is not a general fix.
-- 6. Avoid unnecessary JOINs.
-- 7. WHERE filters rows; HAVING filters aggregated groups.
-- 8. Validate business metrics before reporting results.
-- ============================================================

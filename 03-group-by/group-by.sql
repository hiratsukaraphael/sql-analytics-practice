
SELECT
    customer_id,
    SUM(amount) AS total_revenue
FROM orders
WHERE status = 'completed'
GROUP BY customer_id;

SELECT
    status,
    COUNT(*) AS n_orders
FROM orders
GROUP BY status;

SELECT
    status,
    COUNT(*) AS number_of_orders,
    SUM(amount) AS total_amount,
    AVG(amount) AS average_amount
FROM orders
GROUP BY status;

SELECT
    customer_id,
    SUM(amount) AS total_revenue
FROM orders
WHERE status = 'completed'
GROUP BY customer_id

SELECT
    customer_id,
    SUM(amount) AS total_revenue
FROM orders
WHERE status = 'completed'
GROUP BY customer_id
ORDER BY total_revenue DESC;

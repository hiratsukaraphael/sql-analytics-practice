-- Business question:
-- Which acquisition channels generate customers
-- who actually convert and produce revenue?

SELECT 
    c.acquisition_channel,

    COUNT(DISTINCT c.customer_id) AS customers,

    COUNT(DISTINCT o.customer_id) AS customers_with_orders,

    COUNT(DISTINCT o.customer_id) * 100.0 
        / COUNT(DISTINCT c.customer_id) AS conversion_rate,

    SUM(o.revenue) AS revenue

FROM customers c

LEFT JOIN orders o
    ON c.customer_id = o.customer_id

GROUP BY
    c.acquisition_channel

ORDER BY
    conversion_rate DESC;

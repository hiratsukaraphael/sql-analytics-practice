SELECT
    COUNT(*) AS number_of_orders,
    SUM(amount) AS revenue,
    AVG(amount) AS average_order_value,
    MIN(amount) AS smallest_order,
    MAX(amount) AS largest_order
FROM orders
WHERE status = 'completed';

CREATE TABLE orders (
    order_id INTEGER,
    customer_id INTEGER,
    amount DECIMAL(10,2),
    status VARCHAR(20)
);

INSERT INTO orders VALUES
(1, 101, 45, 'completed'),
(2, 102, 150, 'completed'),
(3, 101, 220, 'cancelled'),
(4, 103, 85, 'completed'),
(5, 104, 175, 'completed'),
(6, 105, 120, 'refunded');

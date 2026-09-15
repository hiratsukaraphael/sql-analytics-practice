/*
SQL Analytics Practice
Topic: Filtering and Sorting

Skills:
- SELECT
- WHERE
- AND
- OR
- IN
- BETWEEN
- ORDER BY
*/


-- Exercise A
-- Return completed orders worth at least $100,
-- showing customer ID and amount, largest first.

SELECT customer_id, amount
FROM orders
WHERE status = 'completed'
  AND amount >= 100
ORDER BY amount DESC;


-- Exercise B
-- Return all columns for cancelled or refunded orders.

SELECT *
FROM orders
WHERE status IN ('cancelled', 'refunded');


-- Exercise C
-- Return completed orders between $50 and $160,
-- ordered from smallest to largest.

SELECT customer_id, amount
FROM orders
WHERE status = 'completed'
  AND amount BETWEEN 50 AND 160
ORDER BY amount ASC;

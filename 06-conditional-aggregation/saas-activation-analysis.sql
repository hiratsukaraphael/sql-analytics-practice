-- ============================================================
-- SaaS Activation Analysis
-- ============================================================

-- SETUP

CREATE TABLE users (
    user_id INT,
    acquisition_channel VARCHAR(20),
    activated INT
);

INSERT INTO users VALUES
    (1, 'Organic', 1),
    (2, 'Organic', 0),
    (3, 'Paid', 1),
    (4, 'Paid', 1),
    (5, 'Referral', 0),
    (6, 'Referral', 1),
    (7, 'Organic', 1),
    (8, 'Paid', 0);


CREATE TABLE subscriptions (
    subscription_id INT,
    user_id INT,
    monthly_revenue DECIMAL(10,2)
);

INSERT INTO subscriptions VALUES
    (201, 1, 20.00),
    (202, 3, 40.00),
    (203, 4, 20.00),
    (204, 6, 40.00);


-- ============================================================
-- BUSINESS QUESTION
-- Compare user activation, paying users, and monthly revenue
-- across acquisition channels.
-- ============================================================

SELECT
    u.acquisition_channel,
    COUNT(DISTINCT u.user_id) AS total_users,

    COUNT(DISTINCT CASE
        WHEN u.activated = 1 THEN u.user_id
    END) AS activated_users,

    COUNT(DISTINCT CASE
        WHEN u.activated = 1 THEN u.user_id
    END) * 100.0
        / COUNT(DISTINCT u.user_id) AS activation_rate,

    COUNT(DISTINCT s.user_id) AS paying_users,

    SUM(s.monthly_revenue) AS monthly_revenue

FROM users AS u

LEFT JOIN subscriptions AS s
    ON u.user_id = s.user_id

GROUP BY
    u.acquisition_channel

ORDER BY
    activation_rate DESC;

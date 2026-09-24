SELECT
    channel,
    device,
    COUNT(*) AS visitors,
    SUM(CASE WHEN purchased = 1 THEN 1 ELSE 0 END) AS purchases,
    100.0 * SUM(CASE WHEN purchased = 1 THEN 1 ELSE 0 END)
        / COUNT(*) AS conversion_rate
FROM visitors
GROUP BY channel, device
HAVING COUNT(*) >= 2;

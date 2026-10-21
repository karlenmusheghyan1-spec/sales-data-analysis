
SELECT
    SUBSTR(date, 1, 7) AS month,
    SUM(quantity * unit_price) AS monthly_revenue
FROM sales
GROUP BY SUBSTR(date, 1, 7)
ORDER BY monthly_revenue DESC;
-- Revenue by Category
SELECT
    category,
    SUM(quantity * unit_price) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;
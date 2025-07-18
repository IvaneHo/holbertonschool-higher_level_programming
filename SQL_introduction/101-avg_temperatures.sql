-- Displays the average temperature (Fahrenheit) by city, ordered from highest to lowest
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;

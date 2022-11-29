-- Imports a table into hbtn_0c_0 database
-- and displays average temperature (Fahrenheit) by city ordered by temp DESC
SELECT city AVG(value) AS avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC

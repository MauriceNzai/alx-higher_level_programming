-- Imports a table into hbtn_0c_0 database
-- Displays top 3 of cities temperature during July & Aug ordered by temp DESC
SELECT city, AVG(value) AS avg_temp FROM
(SELECT city, month, value FROM temperatures WHERE month=7 OR month=8) as A
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;

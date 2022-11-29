-- Imports a table into hbtn_0c_0 database
-- Displays max temperature of each state ordered by state name
SELECT state, MAX(value) AS max_temp FROM temperatures ORDER BY state;

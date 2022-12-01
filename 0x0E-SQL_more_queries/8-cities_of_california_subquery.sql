-- Lists all cities of California found in the database
-- Results sorted in ascending order by cities.id
-- Name of the database will be passed as an argument of the mysql command

-- create the main query followed by the subquery
SELECT cities.id, cities.name FROM cities
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

-- Lists all cities found in the database
-- Display results as cities.id - cities.name - states.name
-- Results sorted in ascending order by cities.id
-- Name of the database will be passed as an argument of the mysql command

SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

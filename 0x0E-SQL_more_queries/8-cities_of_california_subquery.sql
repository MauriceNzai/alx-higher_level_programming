-- Lists all cities of California found in the database
-- Results sorted in ascending order by cities.id
-- Name of the database will be passed as an argument of the mysql command

-- use the new database
use hbtn_0d_usa;
-- create the main query followed by the subquery
SELECT cities.id, cities.name FROM cities WHERE (
	state_id = SELECT id FROM states WHERE name='California')
	ORDER BY cities.id ASC;

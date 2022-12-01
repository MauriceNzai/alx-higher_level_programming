-- Lists all shows found in the database that have at least one genre linked
-- Display results as tv_shows.title - tv_showgenres.genre_id
-- Results sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Name of the database will be passed as an argument of the mysql command

SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

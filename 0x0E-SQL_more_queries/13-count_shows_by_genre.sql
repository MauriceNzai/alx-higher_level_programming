-- List tv shows and their genres
-- List all genres from the database and
-- display the number of shows linked to each genre

SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv.genres_id
GROUP BY genre
ORDER BY number_of_shows DESC;

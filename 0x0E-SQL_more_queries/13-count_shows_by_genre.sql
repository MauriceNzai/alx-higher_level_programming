-- genre id by show
SELECT tv_genre.name AS genre,
COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv.genres_id
GROUP BY genre
ORDER BY number_of_shows DESC;

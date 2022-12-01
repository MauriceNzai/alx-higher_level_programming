-- Lists all shows found in the database that have at least one genre linked
-- Display results as tv_shows.title - tv_showgenres.genre_id
-- Results sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Name of the database will be passed as an argument of the mysql command

SELECT ts.title, tg.genre_id FROM tv_shows ts, tv_show_genres tg
WHERE ts.id = tg.show_id
ORDER BY ts.title ASC, tg.genre_id ASC;

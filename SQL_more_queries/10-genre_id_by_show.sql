-- Script to list all TV shows with at least one genre linked from hbtn_0d_tvshows
-- Each record includes tv_shows.title and tv_show_genres.genre_id
-- Results are sorted by tv_shows.title and tv_show_genres.genre_id in ascending order
-- Only one SELECT statement is used

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;


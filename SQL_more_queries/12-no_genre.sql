-- Script to list all TV shows without a genre from hbtn_0d_tvshows
-- Each record displays tv_shows.title and tv_show_genres.genre_id (NULL for genre_id)
-- Results are sorted by tv_shows.title and tv_show_genres.genre_id in ascending order
-- Only one SELECT statement is used

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;


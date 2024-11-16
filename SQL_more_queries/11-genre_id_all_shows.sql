-- Script to list all TV shows with their genre IDs from hbtn_0d_tvshows
-- If a show does not have a genre, NULL is displayed for genre_id
-- Results are sorted by tv_shows.title and tv_show_genres.genre_id in ascending order
-- Only one SELECT statement is used

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;


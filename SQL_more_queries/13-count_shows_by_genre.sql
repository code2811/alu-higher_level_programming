-- Ensure you are using the correct database
USE hbtn_0d_tvshows;

-- List genres and the count of shows linked to each genre
SELECT tv_show_genres.genre_id AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY tv_show_genres.genre_id
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;


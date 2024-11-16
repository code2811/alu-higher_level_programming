-- Script to list all genres and the number of shows linked to each in hbtn_0d_tvshows
-- Each record displays the genre and the count of shows linked to it
-- Genres with no shows linked are not displayed
-- Results are sorted by the number of shows linked in descending order

SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
INNER JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;


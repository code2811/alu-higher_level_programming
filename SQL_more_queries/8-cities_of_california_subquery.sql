-- Script to list all cities of California from the database hbtn_0d_usa
-- The script uses a subquery to find cities without using the JOIN keyword
-- Results are sorted in ascending order by cities.id

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;


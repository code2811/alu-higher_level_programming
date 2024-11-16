-- Script to list all cities in the database hbtn_0d_usa
-- Each record includes cities.id, cities.name, and states.name
-- Results are sorted in ascending order by cities.id
-- Only one SELECT statement is used

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;


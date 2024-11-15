-- This script lists all records with a score >= 10 from the table 'second_table'.
-- Results display 'score' and 'name' in this order and are ordered by score in descending order.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;


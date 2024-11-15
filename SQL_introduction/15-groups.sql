-- This script lists the number of records with the same score in the table 'second_table'.
-- Results display 'score' and the count of records for each score, labeled as 'number'.
-- The list is sorted by the count of records in descending order.

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;


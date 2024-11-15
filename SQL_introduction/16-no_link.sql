-- Lists all records with name values from second_table ordered by score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

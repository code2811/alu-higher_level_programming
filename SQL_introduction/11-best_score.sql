= 10">
-- Lists all records with score >= 10 from second_table ordered by score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;


This SQL script:
1. Selects the `score` and `name` columns (in that order)
2. From the `second_table`
3. Filters records using `WHERE score >= 10` to only show scores of 10 or higher
4. Orders results by `score` in descending order (`DESC`) to show highest scores first

When you run this script:
```bash
mysql -hlocalhost -uroot -p hbtn_0c_0 < 11-best_score.sql
```

The output will show only records where the score is greater than or equal to 10, ordered from highest to lowest score.

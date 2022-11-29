-- Lists number of records with same score in second_table of hbtn_0c_0
-- Result should display score, number of records for the score label=number
-- Sorted by number of records descending
-- The database name will be passed as argument of mysql command
SELECT score, count(*) AS 'number' FROM second_table
GROUP BY score ORDER BY score DESC;

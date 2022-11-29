-- Lists records of second_table in database hbtn_0c_0 where score >= 10
-- Displaying the name and score, ordered by score, descending oreder
-- The database name will be passed as argument of mysql command
SELECT score, name FROM second_table WHERE score>= 10 ORDER BY score DESC;

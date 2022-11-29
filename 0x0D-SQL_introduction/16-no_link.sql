-- Lists records of second_table of hbtn_0c_0
-- Leaving out rows without a name value
-- Result should display score, name in descending order
-- The database name will be passed as argument of mysql command
SELECT score, name FROM second_table WHERE name != '' ORDER BY score DESC;

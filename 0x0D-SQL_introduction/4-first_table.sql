-- This script creates a table in MySQL server database
-- The database will be passed as argument of mysql command
-- If the table already exists, the script should not fail
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));

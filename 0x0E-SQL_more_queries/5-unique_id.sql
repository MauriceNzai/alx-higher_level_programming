-- Creates a table unique_id with default and unique value on MySQL server
-- Name of the database will be passed as an argument of the mysql command
-- Script should not fail if table already exists
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE, name VARCHAR(256));

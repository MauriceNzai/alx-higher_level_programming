-- Creates a table force_name on MySQL server
-- Name of the database will be passed as an argument of the mysql command
-- Script should not fail if table already exists
CREATE TABLE IF NOT EXISTS 'force_name' ('id' INT, 'name' VARCHAR(256) NOT NULL);

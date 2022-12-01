-- Creates a table id_not_null with default value on MySQL server
-- Name of the database will be passed as an argument of the mysql command
-- Script should not fail if table already exists
CREATE TABLE IF NOT EXISTS 'id_not_null'
(id INT DEFAULT 1, name VARCHAR(256));

-- Creates a database and a table unique_id, auto generated,
-- can't be null and is primary key
-- Name of the database will be passed as an argument of the mysql command
-- Script should not fail if table and/or database already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
-- use the new database
use hbtn_0d_usa;
-- create the new table
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL AUTO_INCREMENT UNIQUE,
       	name VARCHAR(256) NOT NULL,
       	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCE states(id));

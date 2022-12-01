-- Creates u database and a user with only select in the database
-- Sets user password and script should not fail if database and/or user exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Add priviledges to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

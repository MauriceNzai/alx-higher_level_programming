-- Creates user with all previledges on MySQL server
-- Sets user password and script should not fail if user exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- Add priviledges to the user
GRANT ALL PRIVILEDGES ON *.* TO 'user_0d_1'@'localhost';
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

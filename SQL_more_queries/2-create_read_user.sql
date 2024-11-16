-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- First revoke all privileges (if any) to ensure clean state
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_2'@'localhost';

-- Grant only SELECT privilege on the specific database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to ensure changes take effect
FLUSH PRIVILEGES;

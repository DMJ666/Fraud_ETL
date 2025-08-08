-- Create fraud-only user
CREATE USER fraud_user WITH PASSWORD 'fraud_pass';

-- Create fraud database
CREATE DATABASE fraud_db OWNER fraud_user;

-- Revoke superuser access to fraud_db (if required)
REVOKE ALL ON DATABASE fraud_db FROM admin;

-- Grant permissions to fraud_user
GRANT CONNECT ON DATABASE fraud_db TO fraud_user;
GRANT USAGE ON SCHEMA public TO fraud_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO fraud_user;


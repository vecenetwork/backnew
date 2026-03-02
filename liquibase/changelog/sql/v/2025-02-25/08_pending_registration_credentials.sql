--liquibase formatted sql

--changeset ilya:add_credentials_to_pending_registrations

ALTER TABLE pending_registrations
ADD COLUMN username VARCHAR(50),
ADD COLUMN password_hash TEXT;

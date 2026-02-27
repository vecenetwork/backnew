--liquibase formatted sql

--changeset m.kroll:11
--comment: Add social_link column to users table

ALTER TABLE users ADD COLUMN IF NOT EXISTS social_link VARCHAR(255);

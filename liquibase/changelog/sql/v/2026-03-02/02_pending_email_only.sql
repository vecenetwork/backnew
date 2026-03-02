--liquibase formatted sql
--changeset m.kroll:2026-03-02-02

-- Allow email-only signup: username and password_hash set at activation
ALTER TABLE pending_registrations ALTER COLUMN username DROP NOT NULL;
ALTER TABLE pending_registrations ALTER COLUMN password_hash DROP NOT NULL;

--liquibase formatted sql

--changeset m.kroll:2026-03-02-01

CREATE TABLE pending_registrations (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    username VARCHAR(50) NOT NULL,
    password_hash TEXT NOT NULL,
    token VARCHAR(64) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL
);

CREATE INDEX idx_pending_registrations_token ON pending_registrations(token);
CREATE INDEX idx_pending_registrations_expires_at ON pending_registrations(expires_at);

--liquibase formatted sql

--changeset m.kroll:1

CREATE TABLE barrier_tokens (
    token VARCHAR(255) PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--liquibase formatted sql

--changeset m.kroll:7

CREATE TABLE waitlist (
    id SERIAL PRIMARY KEY,
    country VARCHAR(100) NOT NULL,
    gender user_gender NOT NULL,
    birthday DATE NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

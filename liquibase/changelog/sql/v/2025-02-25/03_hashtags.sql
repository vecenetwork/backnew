--liquibase formatted sql

--changeset m.kroll:3

CREATE TABLE hashtags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

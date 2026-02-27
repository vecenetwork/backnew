-- liquibase formatted sql

-- changeset gemini:2
ALTER TABLE question_options ADD COLUMN IF NOT EXISTS count INT NOT NULL DEFAULT 0;
ALTER TABLE question_options ADD COLUMN IF NOT EXISTS percentage FLOAT NOT NULL DEFAULT 0;
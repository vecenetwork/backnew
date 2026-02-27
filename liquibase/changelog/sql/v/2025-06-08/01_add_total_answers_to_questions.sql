-- liquibase formatted sql

-- changeset gemini:1
ALTER TABLE questions ADD COLUMN IF NOT EXISTS total_answers INT NOT NULL DEFAULT 0; 
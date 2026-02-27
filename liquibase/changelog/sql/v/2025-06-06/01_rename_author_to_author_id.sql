--liquibase formatted sql

--changeset author-id-migration:1
--comment: Rename author columns to author_id for better naming convention

-- Rename author column to author_id in questions table
ALTER TABLE questions RENAME COLUMN author TO author_id;

-- Rename author column to author_id in question_options table  
ALTER TABLE question_options RENAME COLUMN author TO author_id;

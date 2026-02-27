--liquibase formatted sql

--changeset m.kroll:3

CREATE TYPE user_role AS ENUM ('user', 'admin');
CREATE TYPE user_gender AS ENUM  ('Male', 'Female', 'Other');
CREATE TYPE setting_show_name_option AS ENUM ('Name', 'Username');
CREATE TYPE setting_show_question_results AS ENUM ('Nobody', 'People I Follow', 'People Following Me', 'All Connections', 'All');


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    birthday DATE NOT NULL,
    country_id INT REFERENCES countries(id) ON DELETE SET NULL,
    gender user_gender NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    profile_picture VARCHAR(255), -- Stores the file path or URL of the profile picture
    role user_role NOT NULL DEFAULT 'user'
);

CREATE TABLE user_settings (
    id SERIAL PRIMARY KEY,
    user_id INT UNIQUE NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    show_name_option setting_show_name_option DEFAULT 'Name',
    show_question_results setting_show_question_results DEFAULT 'All',
    allow_results_in_digests BOOLEAN DEFAULT TRUE,
    receive_digests BOOLEAN DEFAULT TRUE
);


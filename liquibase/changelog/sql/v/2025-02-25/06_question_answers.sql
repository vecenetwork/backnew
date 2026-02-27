--liquibase formatted sql

--changeset m.kroll:6

-- Table: question
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    author INTEGER REFERENCES users(id) ON DELETE CASCADE,
    text TEXT NOT NULL,
    max_options INTEGER NOT NULL CHECK (max_options > 0),
    active_till TIMESTAMP NOT NULL,
    allow_user_options BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),

    -- Audience filters
    gender TEXT[],         -- e.g., ['male', 'female', 'non-binary']
    country_id INTEGER[],  -- e.g., [1, 2, 3]
    age INT4RANGE          -- e.g., [18,30)
);


-- Table: question_hashtag_links (many-to-many)
CREATE TABLE question_hashtag_links (
    question_id INTEGER REFERENCES questions(id) ON DELETE CASCADE,
    hashtag_id INTEGER REFERENCES hashtags(id) ON DELETE CASCADE,
    PRIMARY KEY (question_id, hashtag_id)
);

-- Table: question_options
CREATE TABLE question_options (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(id) ON DELETE CASCADE,
    text TEXT NOT NULL,
    position INTEGER NOT NULL,  -- for ordering options
    author INTEGER REFERENCES users(id),
    by_question_author BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),

    UNIQUE (question_id, position)
);

-- Table: answers
CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT NOW(),

    -- user can answer a question only once
    UNIQUE (question_id, user_id)
);

-- Table: answer_options
CREATE TABLE answer_options (
    answer_id INTEGER REFERENCES answers(id) ON DELETE CASCADE,
    option_id INTEGER REFERENCES question_options(id) ON DELETE CASCADE,
    PRIMARY KEY (answer_id, option_id)
);


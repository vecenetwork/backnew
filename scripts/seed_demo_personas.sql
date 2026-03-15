-- =============================================================
-- VECE Demo Personas Seed
-- Run once in Supabase SQL Editor
-- =============================================================

BEGIN;

-- ── 1. Demo users ──────────────────────────────────────────────
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Friedrich', 'Nietzsche', 'nietzsche', 'demo.nietzsche@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1844-10-15', 'Male', TRUE, TRUE, 'user', 'Philosopher. 1844–1900. Answers based on verified writings.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Leonardo', 'da Vinci', 'davinci', 'demo.davinci@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1452-04-15', 'Male', TRUE, TRUE, 'user', 'Artist & scientist. 1452–1519. Answers based on verified notebooks.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Sigmund', 'Freud', 'freud', 'demo.freud@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1856-05-06', 'Male', TRUE, TRUE, 'user', 'Psychoanalyst. 1856–1939. Answers based on verified writings.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Oscar', 'Wilde', 'wilde', 'demo.wilde@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1854-10-16', 'Male', TRUE, TRUE, 'user', 'Writer & wit. 1854–1900. Answers based on verified works.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Marie', 'Curie', 'curie', 'demo.curie@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1867-11-07', 'Female', TRUE, TRUE, 'user', 'Physicist & chemist. 1867–1934. Answers based on verified writings.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Leo', 'Tolstoy', 'tolstoy', 'demo.tolstoy@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1828-09-09', 'Male', TRUE, TRUE, 'user', 'Novelist & moralist. 1828–1910. Answers based on verified works.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Albert', 'Einstein', 'einstein', 'demo.einstein@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1879-03-14', 'Male', TRUE, TRUE, 'user', 'Physicist. 1879–1955. Answers based on verified writings & interviews.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Coco', 'Chanel', 'chanel', 'demo.chanel@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1883-08-19', 'Female', TRUE, TRUE, 'user', 'Fashion designer. 1883–1971. Answers based on verified interviews.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Charles', 'Darwin', 'darwin', 'demo.darwin@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1809-02-12', 'Male', TRUE, TRUE, 'user', 'Naturalist. 1809–1882. Answers based on verified writings.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Frida', 'Kahlo', 'kahlo', 'demo.kahlo@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1907-07-06', 'Female', TRUE, TRUE, 'user', 'Painter. 1907–1954. Answers based on verified letters & diary.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;

-- ── 2. user_settings ───────────────────────────────────────────
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.nietzsche@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.davinci@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.freud@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.wilde@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.curie@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.tolstoy@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.einstein@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.chanel@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.darwin@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.kahlo@vece.ai'
ON CONFLICT (user_id) DO NOTHING;

-- ── 3. Questions, options, hashtags, answers ───────────────────

-- Q1: What is the purpose of human life?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What is the purpose of human life?', 2, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What is the purpose of human life?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is the purpose of human life?', 2, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To live as if everything is a miracle', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To become who you truly are', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To love and to work', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To create something that outlasts you', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To serve others and reduce suffering', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Existentialism' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Purpose' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Philosophy' ON CONFLICT DO NOTHING;
  END IF;


    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q2: What does it mean to truly know yourself?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What does it mean to truly know yourself?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What does it mean to truly know yourself?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What does it mean to truly know yourself?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To understand your unconscious desires and fears', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To know what you value and live by it', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To observe yourself as you observe the world', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To accept your contradictions without shame', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To question every belief you were given', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Identity' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Psychology' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'SelfImprovement' ON CONFLICT DO NOTHING;
  END IF;


    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- darwin
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.darwin@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.darwin@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q3: Is suffering a necessary part of life?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'Is suffering a necessary part of life?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'Is suffering a necessary part of life?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'Is suffering a necessary part of life?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Yes — what does not kill me makes me stronger', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Yes — suffering is the source of all great art', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'It is inevitable, but the response is a choice', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'No — it is a problem to be solved, not endured', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Yes — it reveals what we truly are', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Existentialism' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'MentalHealth' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Resilience' ON CONFLICT DO NOTHING;
  END IF;


    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- chanel
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.chanel@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.chanel@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q4: What is love at its core?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What is love at its core?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What is love at its core?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is love at its core?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'The desire to possess and be possessed', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'The only sane response to an insane world', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To love and be loved is to feel the sun from both sides', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'The complete surrender of oneself to another', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A force that gives meaning to everything else', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Love' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Romance' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Relationships' ON CONFLICT DO NOTHING;
  END IF;


    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- chanel
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.chanel@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.chanel@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- darwin
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.darwin@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.darwin@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q5: Can a person be truly happy alone?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'Can a person be truly happy alone?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'Can a person be truly happy alone?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'Can a person be truly happy alone?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Yes — solitude is necessary for depth of thought', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Yes — I am never less alone than when alone', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'No — human beings need attachment to flourish', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Happiness requires someone to share it with', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'It depends entirely on what you do with solitude', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Happiness' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Loneliness' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Solitude' ON CONFLICT DO NOTHING;
  END IF;


    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- darwin
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.darwin@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.darwin@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q6: What destroys a relationship faster than anything?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What destroys a relationship faster than anything?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What destroys a relationship faster than anything?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What destroys a relationship faster than anything?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Dishonesty — it poisons everything it touches', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Contempt — it is the opposite of respect', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Repression — hiding what you feel', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Indifference — the opposite of love is not hate', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'The inability to admit you were wrong', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Relationships' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Friendship' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Honesty' ON CONFLICT DO NOTHING;
  END IF;


    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- chanel
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.chanel@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.chanel@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q7: What drives human progress?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What drives human progress?', 2, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What drives human progress?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What drives human progress?', 2, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Imagination — it is more important than knowledge', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Curiosity — the desire to understand everything', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Necessity and the will to overcome it', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'The refusal to accept that things cannot be better', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Gradual adaptation and accumulated small changes', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Science' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Innovation' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Curiosity' ON CONFLICT DO NOTHING;
  END IF;


    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- darwin
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.darwin@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.darwin@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q8: Should science and religion be in conflict?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'Should science and religion be in conflict?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'Should science and religion be in conflict?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'Should science and religion be in conflict?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'No — science without religion is lame, religion without science is blind', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Yes — religion answers questions science has not yet reached', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'No — religion is simply pre-scientific explanation', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Science replaces religion as knowledge grows', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'They speak different languages about different things', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Religion' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Science' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Ethics' ON CONFLICT DO NOTHING;
  END IF;


    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- darwin
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.darwin@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.darwin@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q9: Is truth absolute or does it depend on who is looking?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'Is truth absolute or does it depend on who is looking?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'Is truth absolute or does it depend on who is looking?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'Is truth absolute or does it depend on who is looking?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'There are no facts, only interpretations', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Truth is what survives rigorous testing', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Objective truth exists but most people avoid it', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Truth is rarely pure and never simple', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Scientific truth accumulates slowly and imperfectly', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Logic' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Philosophy' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'CriticalThinking' ON CONFLICT DO NOTHING;
  END IF;


    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- darwin
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.darwin@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.darwin@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q10: What is art for?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What is art for?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What is art for?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is art for?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To paint my own reality, not the reality imposed on me', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To express what words cannot reach', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To tell truth through beautiful lies', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To unite people across all differences', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To show what it feels like to be alive', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Art' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Creativity' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Culture' ON CONFLICT DO NOTHING;
  END IF;


    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- chanel
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.chanel@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.chanel@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q11: Is beauty objective or in the eye of the beholder?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'Is beauty objective or in the eye of the beholder?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'Is beauty objective or in the eye of the beholder?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'Is beauty objective or in the eye of the beholder?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Beauty is entirely subjective — there is no standard', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Beauty follows universal mathematical proportions', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Beauty is what we project onto what we desire', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Elegance is the right balance — never more, never less', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Beauty in nature follows deep evolutionary logic', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Art' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Philosophy' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Aesthetics' ON CONFLICT DO NOTHING;
  END IF;


    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- chanel
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.chanel@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.chanel@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- darwin
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.darwin@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.darwin@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q12: What should education teach above all else?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What should education teach above all else?', 2, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What should education teach above all else?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What should education teach above all else?', 2, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'How to think, not what to think', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'How to observe carefully and question everything', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Moral principles — knowledge without ethics is dangerous', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'That most of what you believe is wrong', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'How to endure uncertainty and keep going', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Education' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'SelfImprovement' ON CONFLICT DO NOTHING;
  END IF;


    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- darwin
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.darwin@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.darwin@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q13: Is ambition a virtue or a vice?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'Is ambition a virtue or a vice?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'Is ambition a virtue or a vice?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'Is ambition a virtue or a vice?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A virtue — the will to power is what drives humanity forward', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A virtue when directed at something larger than yourself', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A vice when it replaces love and connection', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Neither — it is neutral, only the object of ambition matters', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A virtue — those without it live other people''s lives', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Ambition' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'PersonalGrowth' ON CONFLICT DO NOTHING;
  END IF;


    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- chanel
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.chanel@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.chanel@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q14: What is more dangerous: ignorance or certainty?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What is more dangerous: ignorance or certainty?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What is more dangerous: ignorance or certainty?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is more dangerous: ignorance or certainty?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Certainty — it closes the mind entirely', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Ignorance — you cannot act well on what you do not know', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Certainty — conviction is the greatest enemy of truth', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Both equally — they are two forms of the same blindness', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Certainty — especially in moral matters', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'CriticalThinking' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Ethics' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Logic' ON CONFLICT DO NOTHING;
  END IF;


    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- darwin
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.darwin@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.darwin@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q15: What does the way you dress say about you?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What does the way you dress say about you?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What does the way you dress say about you?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What does the way you dress say about you?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Everything — fashion is the armor to survive everyday life', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Only what you want others to see — nothing more', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Less than people think — ideas matter more than clothes', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'It reflects your inner state whether you intend it or not', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Simplicity is the ultimate sophistication', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Fashion' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Identity' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Style' ON CONFLICT DO NOTHING;
  END IF;


    -- chanel
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.chanel@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.chanel@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q16: What is the greatest waste of a human life?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What is the greatest waste of a human life?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What is the greatest waste of a human life?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is the greatest waste of a human life?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Living for the approval of others', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Not satisfying your curiosity about the world', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Refusing to face what is true about yourself', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Spending it on things that do not bring joy', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Accepting the life handed to you without question', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Purpose' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Existentialism' ON CONFLICT DO NOTHING;
  END IF;


    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- chanel
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.chanel@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.chanel@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q17: Is it better to live a short intense life or a long quiet on
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'Is it better to live a short intense life or a long quiet one?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'Is it better to live a short intense life or a long quiet one?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'Is it better to live a short intense life or a long quiet one?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Short and intense — better to burn than to fade', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Long — you need time to understand anything deeply', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'It depends entirely on what fills it', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Long — a life of service is never wasted', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Intense — the only life that leaves a mark', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Purpose' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Happiness' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
  END IF;


    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- darwin
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.darwin@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.darwin@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- chanel
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.chanel@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.chanel@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q18: What role does nature play in human happiness?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What role does nature play in human happiness?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What role does nature play in human happiness?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What role does nature play in human happiness?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'It is essential — we are animals and belong in it', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Nature is a model for everything beautiful and true', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'It soothes but cannot replace human connection', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'It reminds us of what we actually are, beneath everything', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Nature was my laboratory — it was where I felt most alive', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Nature' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Happiness' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Health' ON CONFLICT DO NOTHING;
  END IF;


    -- darwin
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.darwin@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.darwin@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q19: What is the hardest thing to change in a person?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What is the hardest thing to change in a person?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What is the hardest thing to change in a person?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is the hardest thing to change in a person?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Their childhood — it shapes everything that follows', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Their values — they are built over decades', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Their beliefs about themselves', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Their habits — behavior outlasts intention', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Their fear of being wrong', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Psychology' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Habits' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'PersonalGrowth' ON CONFLICT DO NOTHING;
  END IF;


    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- darwin
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.darwin@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.darwin@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- wilde
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.wilde@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.wilde@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q20: What does courage look like in everyday life?
INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
SELECT id, 'What does courage look like in everyday life?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
FROM users WHERE email = 'demo.nietzsche@vece.ai'
RETURNING id;

DO $$
DECLARE
  qid INT;
  aid INT;
  inserted_count INT;
BEGIN
  SELECT id INTO qid FROM questions
  WHERE text = 'What does courage look like in everyday life?'
  ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What does courage look like in everyday life?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.nietzsche@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Saying what you believe when no one else will', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Continuing your work when results feel far away', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Being honest with yourself about who you are', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Choosing to create when the world offers destruction', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Facing the unknown without needing certainty first', 4, NULL, TRUE, NOW());
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Courage' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Resilience' ON CONFLICT DO NOTHING;
  END IF;


    -- nietzsche
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.nietzsche@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.nietzsche@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- curie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.curie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.curie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- freud
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.freud@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.freud@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- kahlo
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.kahlo@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.kahlo@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- einstein
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.einstein@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.einstein@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- davinci
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.davinci@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.davinci@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- tolstoy
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.tolstoy@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.tolstoy@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- chanel
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.chanel@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;

    GET DIAGNOSTICS inserted_count = ROW_COUNT;
    IF inserted_count > 0 THEN
      SELECT a.id INTO aid FROM answers a
      JOIN users u ON u.id = a.user_id WHERE u.email = 'demo.chanel@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- ── 4. Recalculate counts ──────────────────────────────────────
UPDATE question_options qo
SET count = sub.cnt
FROM (
  SELECT option_id, COUNT(*) AS cnt FROM answer_options GROUP BY option_id
) sub
WHERE qo.id = sub.option_id;

UPDATE question_options qo
SET percentage = qo.count * 100.0 / NULLIF(q.total_answers, 0)
FROM questions q WHERE q.id = qo.question_id;

UPDATE questions q
SET total_answers = sub.cnt
FROM (
  SELECT question_id, COUNT(*) AS cnt FROM answers GROUP BY question_id
) sub
WHERE q.id = sub.question_id;

COMMIT;

-- Done. 10 personas, 20 questions, 160 answers.
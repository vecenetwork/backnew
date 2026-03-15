-- =============================================================
-- VECE Proust Questionnaire Seed
-- 15 public figures, 16 questions, ~200 answer records
-- Run once in Supabase SQL Editor
-- =============================================================

BEGIN;

-- ── 1. Users ────────────────────────────────────────────────
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Marcel', 'Proust', 'marcelproust', 'demo.proust@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1871-07-10', 'Male', TRUE, TRUE, 'user', 'Writer. 1871–1922. Answered his own questionnaire twice.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('David', 'Bowie', 'davidbowie', 'demo.bowie@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1947-01-08', 'Male', TRUE, TRUE, 'user', 'Musician & artist. 1947–2016. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Cate', 'Blanchett', 'cateblanchett', 'demo.blanchett@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1969-05-14', 'Female', TRUE, TRUE, 'user', 'Actor. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Stephen', 'Fry', 'stephenfry', 'demo.fry@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1957-08-24', 'Male', TRUE, TRUE, 'user', 'Writer & actor. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Malala', 'Yousafzai', 'malala', 'demo.malala@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1997-07-12', 'Female', TRUE, TRUE, 'user', 'Activist & Nobel laureate. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Toni', 'Morrison', 'tonimorrison', 'demo.morrison@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1931-02-18', 'Female', TRUE, TRUE, 'user', 'Nobel Prize novelist. 1931–2019. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Anthony', 'Hopkins', 'anthonyhopkins', 'demo.ahopkins@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1937-12-31', 'Male', TRUE, TRUE, 'user', 'Actor. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Patti', 'Smith', 'pattismith', 'demo.psmith@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1946-12-30', 'Female', TRUE, TRUE, 'user', 'Musician & poet. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Chimamanda', 'Adichie', 'chimamanda', 'demo.adichie@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1977-09-15', 'Female', TRUE, TRUE, 'user', 'Novelist. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Barack', 'Obama', 'barackobama', 'demo.obama@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1961-08-04', 'Male', TRUE, TRUE, 'user', '44th US President. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Bjork', 'Gudmundsdottir', 'bjork', 'demo.bjork@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1965-11-21', 'Female', TRUE, TRUE, 'user', 'Musician. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Judi', 'Dench', 'judidench', 'demo.dench@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1934-12-09', 'Female', TRUE, TRUE, 'user', 'Actor. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Salman', 'Rushdie', 'salmanrushdie', 'demo.rushdie@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1947-06-19', 'Male', TRUE, TRUE, 'user', 'Novelist. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Zadie', 'Smith', 'zadiesmith', 'demo.zsmith@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1975-10-25', 'Female', TRUE, TRUE, 'user', 'Novelist. Vanity Fair.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;
INSERT INTO users (name, surname, username, email, password_hash, birthday, gender, is_verified, is_active, role, description, created_at, updated_at)
VALUES ('Pele', 'Nascimento', 'pele', 'demo.pele@vece.ai', '$2b$12$demoVECEplaceholderXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '1940-10-23', 'Male', TRUE, TRUE, 'user', 'Footballer. 1940–2022. Documented interviews.', NOW(), NOW())
ON CONFLICT (email) DO NOTHING;

-- ── 2. user_settings ───────────────────────────────────────
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.proust@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.bowie@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.blanchett@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.fry@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.malala@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.morrison@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.ahopkins@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.psmith@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.adichie@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.obama@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.bjork@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.dench@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.rushdie@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.zsmith@vece.ai'
ON CONFLICT (user_id) DO NOTHING;
INSERT INTO user_settings (user_id)
SELECT id FROM users WHERE email = 'demo.pele@vece.ai'
ON CONFLICT (user_id) DO NOTHING;

-- ── 3. Questions, options, hashtags, answers ───────────────

-- Q1: What is your idea of perfect happiness?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'What is your idea of perfect happiness?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is your idea of perfect happiness?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To love and be loved in return', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Freedom — to do exactly what I want, when I want', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Being present in a moment so completely you forget time', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A good book, a warm room, and no obligations', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Seeing people I love safe and fulfilled', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Solitude with meaningful work', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A long walk alone with nowhere to be', 6, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Being on stage or lost in a role', 7, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Happiness' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Purpose' ON CONFLICT DO NOTHING;
  END IF;


    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- anthonyhopkins
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.ahopkins@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.ahopkins@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q2: What is your greatest fear?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'What is your greatest fear?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is your greatest fear?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Being separated from those I love', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Mediocrity — producing work that doesn''t matter', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Not living up to the trust people place in me', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Losing my mind', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Ignorance defeating knowledge', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Cowardice — my own', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Dying before I''ve said what I needed to say', 6, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Boredom — an empty, purposeless existence', 7, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Psychology' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Anxiety' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Identity' ON CONFLICT DO NOTHING;
  END IF;


    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- bjork
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bjork@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bjork@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q3: Which living person do you most admire?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'Which living person do you most admire?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'Which living person do you most admire?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Someone who gave up comfort to do what was right', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A teacher who changed how I saw the world', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Anyone who creates beauty without needing recognition', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Someone raising children with kindness and patience', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A scientist working on problems no one else will touch', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Whoever is fighting hardest for the people with least power', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A writer who tells the truth plainly', 6, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Leadership' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Courage' ON CONFLICT DO NOTHING;
  END IF;


    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- bjork
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bjork@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bjork@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q4: What is the trait you most deplore in yourself?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'What is the trait you most deplore in yourself?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is the trait you most deplore in yourself?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A tendency toward self-doubt at the worst moments', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Impatience — I expect too much too fast', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Vanity — caring too much what others think', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Procrastination dressed up as perfectionism', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A capacity for rage I don''t always control', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Restlessness — I can never just sit still', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Taking on too much because I can''t say no', 6, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Overthinking things that should be simple', 7, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Identity' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'SelfImprovement' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Honesty' ON CONFLICT DO NOTHING;
  END IF;


    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- pele
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.pele@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.pele@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q5: What is the trait you most deplore in others?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'What is the trait you most deplore in others?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is the trait you most deplore in others?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Cruelty — especially casual cruelty', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Dishonesty — especially with oneself', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Stupidity combined with confidence', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Indifference to other people''s suffering', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Pettiness — making small things into big conflicts', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Cowardice dressed up as caution', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Intolerance of difference', 6, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Arrogance without the talent to justify it', 7, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Ethics' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Empathy' ON CONFLICT DO NOTHING;
  END IF;


    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- anthonyhopkins
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.ahopkins@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.ahopkins@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q6: What is your greatest extravagance?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'What is your greatest extravagance?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is your greatest extravagance?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Books — I buy far more than I can read', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Time — I guard it ferociously', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Travel — I need to keep moving', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Flowers — I always have them wherever I live', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Music equipment and sound experimentation', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Feeding everyone who comes to my house', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Sleep — I give it the full respect it deserves', 6, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Art — I surround myself with it', 7, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Happiness' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Style' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
  END IF;


    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- bjork
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bjork@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bjork@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- pele
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.pele@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.pele@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q7: On what occasion do you lie?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'On what occasion do you lie?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'On what occasion do you lie?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'When the truth would cause pain without any benefit', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'When someone needs confidence more than accuracy', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'I try not to — lies compound into larger problems', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To protect people I love from things they cannot change', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Almost never — I find honesty easier in the long run', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'When reality needs a better story', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'To protect my own privacy when people pry', 6, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Honesty' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Ethics' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Relationships' ON CONFLICT DO NOTHING;
  END IF;


    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q8: What do you most dislike about your appearance?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'What do you most dislike about your appearance?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What do you most dislike about your appearance?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Nothing — I''ve made peace with it', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'It distracts people from what I''m actually saying', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'It''s irrelevant — I stopped thinking about it', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'That it changes and I can''t keep up', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'I''m too short', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'The gap between how I feel and how I look', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'I wish I took better care of it when I was younger', 6, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Identity' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'BodyImage' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'SelfEsteem' ON CONFLICT DO NOTHING;
  END IF;


    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- pele
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.pele@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.pele@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- anthonyhopkins
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.ahopkins@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.ahopkins@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q9: Which words or phrases do you most overuse?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'Which words or phrases do you most overuse?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'Which words or phrases do you most overuse?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, '''Extraordinary'' — I find too many things extraordinary', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, '''Interesting'' — when I mean something much stronger', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, '''You know'' — as punctuation more than meaning', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, '''Obviously'' — which is never obvious to others', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, '''Exactly'' — agreeing before I''ve fully listened', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, '''Fine'' — when nothing is fine', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'I repeat myself when I''m excited — the same point, twice', 6, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Humor' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Identity' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Communication' ON CONFLICT DO NOTHING;
  END IF;


    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- pele
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.pele@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.pele@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q10: What or who is the greatest love of your life?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'What or who is the greatest love of your life?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What or who is the greatest love of your life?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Literature — it has never failed me', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Music — it found me before anything else', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'My children', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Language itself — the material I work with', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Football', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'The stage — performing is where I''m most myself', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'The people who stayed when it was difficult', 6, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Ideas — the moment a new one arrives', 7, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Love' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Relationships' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Purpose' ON CONFLICT DO NOTHING;
  END IF;


    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- pele
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.pele@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.pele@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- anthonyhopkins
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.ahopkins@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.ahopkins@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- bjork
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bjork@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bjork@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q11: When and where were you happiest?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'When and where were you happiest?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'When and where were you happiest?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Childhood, before I understood what the world demanded', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'When I was first discovering what I could do', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Right now — I try to make that true each day', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'In the middle of writing something that was working', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'On a pitch, during a game where everything was right', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Whenever I am genuinely lost in someone else''s story', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Early in my career, broke but free', 6, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Any morning with coffee, quiet, and nowhere to be yet', 7, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Happiness' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Nostalgia' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Purpose' ON CONFLICT DO NOTHING;
  END IF;


    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- pele
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.pele@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.pele@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- bjork
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bjork@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bjork@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- anthonyhopkins
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.ahopkins@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.ahopkins@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q12: What is your most treasured possession?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'What is your most treasured possession?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is your most treasured possession?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Letters from people I''ve loved', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A notebook I''ve had for years', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'My health — I took it for granted too long', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A book that changed me when I needed it most', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Nothing material — I''ve lost too much to be attached', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'My passport — it represents everything I''ve earned', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'My first instrument', 6, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'A photograph I can''t replace', 7, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Nostalgia' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Identity' ON CONFLICT DO NOTHING;
  END IF;


    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- anthonyhopkins
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.ahopkins@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.ahopkins@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- bjork
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bjork@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bjork@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- pele
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.pele@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.pele@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q13: What do you consider your greatest achievement?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'What do you consider your greatest achievement?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What do you consider your greatest achievement?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Surviving something that should have broken me', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Still being curious after everything', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Raising children who are better than me', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Writing something that helped someone feel less alone', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Never giving up when every reason said to', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Staying honest in a world that rewards the opposite', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'The work itself — the body of it', 6, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Learning, late, to ask for help', 7, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Ambition' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Purpose' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
  END IF;


    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- anthonyhopkins
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.ahopkins@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.ahopkins@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- bjork
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bjork@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bjork@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- pele
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.pele@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.pele@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q14: If you could change one thing about yourself, what woul
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'If you could change one thing about yourself, what would it be?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'If you could change one thing about yourself, what would it be?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'More courage earlier — I waited too long for some things', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Less need for approval', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'More patience with people who disagree', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'I''d start younger — not waste the early years', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Fewer fears — I''ve let fear make too many decisions', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'More discipline about sleep and the body', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Nothing — the flaws are part of the work', 6, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'I''d learn to rest without guilt', 7, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Identity' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'PersonalGrowth' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'SelfImprovement' ON CONFLICT DO NOTHING;
  END IF;


    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- pele
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.pele@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.pele@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- bjork
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bjork@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bjork@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- anthonyhopkins
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.ahopkins@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.ahopkins@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q15: How would you like to die?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'How would you like to die?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'How would you like to die?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Quickly, while still useful', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Old, with the people I love nearby', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Having finished what I started', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Surprised — not expecting it', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Knowing I did enough', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'With no unfinished regrets — things said, apologies made', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'In my sleep, mid-sentence in a good dream', 6, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'It doesn''t matter how — only that the work outlasts it', 7, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Existentialism' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Purpose' ON CONFLICT DO NOTHING;
  END IF;


    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- anthonyhopkins
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.ahopkins@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.ahopkins@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- bjork
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bjork@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bjork@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- pele
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.pele@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.pele@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- Q16: What is your motto?
DO $$
DECLARE
  qid      INT;
  aid      INT;
  ins_count INT;
BEGIN
  -- skip if already seeded
  SELECT id INTO qid FROM questions WHERE text = 'What is your motto?' ORDER BY id DESC LIMIT 1;

  IF qid IS NULL THEN
    INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options, created_at, gender, country_id, age)
    SELECT id, 'What is your motto?', 1, NOW() + INTERVAL '3650 days', TRUE, NOW(), NULL, NULL, NULL
    FROM users WHERE email = 'demo.proust@vece.ai'
    RETURNING id INTO qid;

    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'The only way out is through', 0, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Be curious, not judgmental', 1, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Do it now — later is the enemy of everything', 2, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Tell the truth. Then run.', 3, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'One book can change the world', 4, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Stay close to anything that makes you glad you are alive', 5, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Be kind — everyone is fighting a hard battle', 6, NULL, TRUE, NOW());
    INSERT INTO question_options (question_id, text, position, author_id, by_question_author, created_at) VALUES (qid, 'Know what you don''t know', 7, NULL, TRUE, NOW());

    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Values' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Purpose' ON CONFLICT DO NOTHING;
    INSERT INTO question_hashtag_links (question_id, hashtag_id) SELECT qid, id FROM hashtags WHERE name = 'Wisdom' ON CONFLICT DO NOTHING;
  END IF;


    -- pattismith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.psmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.psmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- barackobama
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.obama@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.obama@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
    -- davidbowie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bowie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bowie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 2 ON CONFLICT DO NOTHING;    END IF;
    -- salmanrushdie
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.rushdie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.rushdie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 3 ON CONFLICT DO NOTHING;    END IF;
    -- malala
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.malala@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.malala@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- bjork
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.bjork@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.bjork@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 5 ON CONFLICT DO NOTHING;    END IF;
    -- judidench
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.dench@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.dench@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- stephenfry
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.fry@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.fry@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- marcelproust
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.proust@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.proust@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- tonimorrison
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.morrison@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.morrison@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 0 ON CONFLICT DO NOTHING;    END IF;
    -- chimamanda
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.adichie@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.adichie@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 4 ON CONFLICT DO NOTHING;    END IF;
    -- zadiesmith
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.zsmith@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.zsmith@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- cateblanchett
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.blanchett@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.blanchett@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 6 ON CONFLICT DO NOTHING;    END IF;
    -- anthonyhopkins
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.ahopkins@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.ahopkins@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 7 ON CONFLICT DO NOTHING;    END IF;
    -- pele
    INSERT INTO answers (question_id, user_id, created_at)
    SELECT qid, u.id, NOW() FROM users u WHERE u.email = 'demo.pele@vece.ai'
    ON CONFLICT (question_id, user_id) DO NOTHING;
    GET DIAGNOSTICS ins_count = ROW_COUNT;
    IF ins_count > 0 THEN
      SELECT a.id INTO aid FROM answers a JOIN users u ON u.id = a.user_id
      WHERE u.email = 'demo.pele@vece.ai' AND a.question_id = qid;      INSERT INTO answer_options (answer_id, option_id) SELECT aid, id FROM question_options WHERE question_id = qid AND position = 1 ON CONFLICT DO NOTHING;    END IF;
END $$;

-- ── 4. Recalculate counts ──────────────────────────────────
UPDATE question_options qo
SET count = sub.cnt
FROM (SELECT option_id, COUNT(*) AS cnt FROM answer_options GROUP BY option_id) sub
WHERE qo.id = sub.option_id;

UPDATE question_options qo
SET percentage = qo.count * 100.0 / NULLIF(q.total_answers, 0)
FROM questions q WHERE q.id = qo.question_id;

UPDATE questions q
SET total_answers = sub.cnt
FROM (SELECT question_id, COUNT(*) AS cnt FROM answers GROUP BY question_id) sub
WHERE q.id = sub.question_id;

COMMIT;
-- Done: 15 personas, 16 Proust questions.
MUTUALITY = """
WITH my_answers AS (
    SELECT question_id
    FROM answers
    WHERE user_id = :my_id
    AND (:start_date ::timestamp IS NULL OR created_at >= :start_date ::timestamp)
),
other_answers AS (
    SELECT question_id
    FROM answers
    WHERE user_id = :other_id
    AND (:start_date ::timestamp IS NULL OR created_at >= :start_date ::timestamp)
),
common_answers AS (
    SELECT ua.question_id
    FROM my_answers ua
    INNER JOIN other_answers u2a ON ua.question_id = u2a.question_id
),
counts AS (
    SELECT
        (SELECT COUNT(*) FROM my_answers) AS my_total,
        (SELECT COUNT(*) FROM other_answers) AS other_total,
        (SELECT COUNT(*) FROM common_answers) AS common_total
)
SELECT
    common_total::DECIMAL / NULLIF(my_total, 0) AS mutuality,
    my_total,
    other_total,
    common_total
FROM counts;
"""


SIMILARITY = """
WITH
my_answers AS (
    SELECT a.question_id, ao.option_id
    FROM answers a
    JOIN answer_options ao ON ao.answer_id = a.id
    WHERE a.user_id = :my_id
    AND (:start_date ::timestamp IS NULL OR a.created_at >= :start_date ::timestamp)
),
other_answers AS (
    SELECT a.question_id, ao.option_id
    FROM answers a
    JOIN answer_options ao ON ao.answer_id = a.id
    WHERE a.user_id = :other_id
    AND (:start_date ::timestamp IS NULL OR a.created_at >= :start_date ::timestamp)
),
common_questions AS (
    SELECT DISTINCT u1.question_id
    FROM my_answers u1
    INNER JOIN other_answers u2 ON u1.question_id = u2.question_id
),
per_question_similarity AS (
    SELECT
        q.question_id,
        COUNT(DISTINCT u1.option_id) FILTER (WHERE u1.option_id = u2.option_id) AS intersection_count,
        COUNT(DISTINCT u1.option_id) + COUNT(DISTINCT u2.option_id)
            - COUNT(DISTINCT u1.option_id) FILTER (WHERE u1.option_id = u2.option_id) AS union_count
    FROM common_questions q
    LEFT JOIN my_answers u1 ON u1.question_id = q.question_id
    LEFT JOIN other_answers u2 ON u2.question_id = q.question_id
    GROUP BY q.question_id
),
final_similarity AS (
    SELECT
        question_id,
        CASE
            WHEN union_count > 0 THEN intersection_count::DECIMAL / union_count
            ELSE 0
        END AS question_similarity
    FROM per_question_similarity
)
SELECT
    AVG(question_similarity) AS avg_similarity,
    COUNT(*) AS common_total
FROM final_similarity;
"""

MUTUALITY_AND_SIMILARITY = """
WITH my_answers AS (
    SELECT question_id
    FROM answers
    WHERE user_id = :my_id
    AND (:start_date ::timestamp IS NULL OR created_at >= :start_date ::timestamp)
),
other_answers AS (
    SELECT question_id
    FROM answers
    WHERE user_id = :other_id
    AND (:start_date ::timestamp IS NULL OR created_at >= :start_date ::timestamp)
),
common_answers AS (
    SELECT ua.question_id
    FROM my_answers ua
    INNER JOIN other_answers u2a ON ua.question_id = u2a.question_id
),
counts AS (
    SELECT
        (SELECT COUNT(*) FROM my_answers) AS my_total,
        (SELECT COUNT(*) FROM other_answers) AS other_total,
        (SELECT COUNT(*) FROM common_answers) AS common_total
),
similarity_my_answers AS (
    SELECT a.question_id, ao.option_id
    FROM answers a
    JOIN answer_options ao ON ao.answer_id = a.id
    WHERE a.user_id = :my_id
    AND (:start_date ::timestamp IS NULL OR a.created_at >= :start_date ::timestamp)
),
similarity_other_answers AS (
    SELECT a.question_id, ao.option_id
    FROM answers a
    JOIN answer_options ao ON ao.answer_id = a.id
    WHERE a.user_id = :other_id
    AND (:start_date ::timestamp IS NULL OR a.created_at >= :start_date ::timestamp)
),
common_questions AS (
    SELECT DISTINCT u1.question_id
    FROM similarity_my_answers u1
    INNER JOIN similarity_other_answers u2 ON u1.question_id = u2.question_id
),
per_question_similarity AS (
    SELECT
        q.question_id,
        COUNT(DISTINCT u1.option_id) FILTER (WHERE u1.option_id = u2.option_id) AS intersection_count,
        COUNT(DISTINCT u1.option_id) + COUNT(DISTINCT u2.option_id)
            - COUNT(DISTINCT u1.option_id) FILTER (WHERE u1.option_id = u2.option_id) AS union_count
    FROM common_questions q
    LEFT JOIN similarity_my_answers u1 ON u1.question_id = q.question_id
    LEFT JOIN similarity_other_answers u2 ON u2.question_id = q.question_id
    GROUP BY q.question_id
),
final_similarity AS (
    SELECT
        question_id,
        CASE
            WHEN union_count > 0 THEN intersection_count::DECIMAL / union_count
            ELSE 0
        END AS question_similarity
    FROM per_question_similarity
),
similarity_summary AS (
    SELECT
        AVG(question_similarity) AS avg_similarity
    FROM final_similarity
)
SELECT
    c.common_total::DECIMAL / NULLIF(c.my_total, 0) AS mutuality,
    s.avg_similarity,
    c.my_total,
    c.other_total,
    c.common_total
FROM counts c
CROSS JOIN similarity_summary s;
"""
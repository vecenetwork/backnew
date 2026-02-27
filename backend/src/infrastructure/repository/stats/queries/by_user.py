
STATISTICS_BY_USER_ID_PAGINATED = """
WITH UniqueQuestions AS (
    -- First, get a unique list of question IDs based on the user and role.
    -- This is important for correct pagination and avoiding duplicate work.
    SELECT DISTINCT q.id
    FROM questions q
    LEFT JOIN answers a ON q.id = a.question_id
    WHERE
        (:role_filter = 'all' AND (q.author_id = :user_id OR a.user_id = :user_id))
        OR (:role_filter = 'author' AND q.author_id = :user_id)
        OR (:role_filter = 'respondent' AND a.user_id = :user_id)
    ORDER BY q.id DESC
    LIMIT :limit OFFSET :offset
),
QuestionAndRole AS (
    -- Determine the user's role for each unique question
    SELECT
        uq.id,
        -- Determine the role ('author' or 'respondent')
        CASE
            WHEN q.author_id = :user_id THEN 'author'
            ELSE 'respondent'
        END as role
    FROM UniqueQuestions uq
    JOIN questions q on uq.id = q.id
),
QuestionStats AS (
    -- Calculate statistics ONLY for questions where the user is the author
    SELECT
        qr.id as question_id,
        -- Aggregate statistics for age
        jsonb_object_agg(
            COALESCE(age_stats.age_range, 'Unknown'), age_stats.count
        ) FILTER (WHERE age_stats.age_range IS NOT NULL) as answers_by_age,
        
        -- Aggregate statistics for gender
        jsonb_object_agg(
            COALESCE(gender_stats.gender, 'Unknown'), gender_stats.count
        ) FILTER (WHERE gender_stats.gender IS NOT NULL) as answers_by_gender,
        
        -- Aggregate statistics for country
        jsonb_object_agg(
            COALESCE(country_stats.country, 'Unknown'), country_stats.count
        ) FILTER (WHERE country_stats.country IS NOT NULL) as answers_by_country,
        
        -- Get total answers for the question
        (SELECT COUNT(*) FROM answers WHERE answers.question_id = qr.id) as total_answers

    FROM QuestionAndRole qr
    -- AGE
    LEFT JOIN (
        SELECT
            a.question_id,
            CASE
                WHEN u.birthday IS NULL THEN 'Unknown'
                WHEN EXTRACT(YEAR FROM AGE(u.birthday)) < 18 THEN 'Under 18'
                WHEN EXTRACT(YEAR FROM AGE(u.birthday)) BETWEEN 18 AND 24 THEN '18-24'
                WHEN EXTRACT(YEAR FROM AGE(u.birthday)) BETWEEN 25 AND 34 THEN '25-34'
                WHEN EXTRACT(YEAR FROM AGE(u.birthday)) BETWEEN 35 AND 44 THEN '35-44'
                WHEN EXTRACT(YEAR FROM AGE(u.birthday)) BETWEEN 45 AND 54 THEN '45-54'
                WHEN EXTRACT(YEAR FROM AGE(u.birthday)) BETWEEN 55 AND 64 THEN '55-64'
                ELSE '65+'
            END as age_range,
            COUNT(*) as count
        FROM answers a
        JOIN users u ON a.user_id = u.id
        WHERE a.question_id IN (SELECT id FROM QuestionAndRole WHERE role = 'author')
        GROUP BY a.question_id, age_range
    ) as age_stats ON qr.id = age_stats.question_id

    -- GENDER
    LEFT JOIN (
        SELECT
            a.question_id,
            u.gender::text,
            COUNT(*) as count
        FROM answers a
        JOIN users u ON a.user_id = u.id
        WHERE a.question_id IN (SELECT id FROM QuestionAndRole WHERE role = 'author')
        GROUP BY a.question_id, u.gender
    ) as gender_stats ON qr.id = gender_stats.question_id

    -- COUNTRY
    LEFT JOIN (
        SELECT
            a.question_id,
            c.name as country,
            COUNT(*) as count
        FROM answers a
        JOIN users u ON a.user_id = u.id
        JOIN countries c ON u.country_id = c.id
        WHERE a.question_id IN (SELECT id FROM QuestionAndRole WHERE role = 'author')
        GROUP BY a.question_id, c.name
    ) as country_stats ON qr.id = country_stats.question_id
    
    WHERE qr.role = 'author' -- IMPORTANT: Only calculate stats if the user is the author
    GROUP BY qr.id
)
-- Final SELECT statement to bring it all together
SELECT
    uq.id,
    qr.role,
    -- Include statistics if the user is the author
    CASE
        WHEN qr.role = 'author' THEN jsonb_build_object(
            'total_answers', COALESCE(qs.total_answers, 0),
            'answers_by_age', COALESCE(qs.answers_by_age, '{}'::jsonb),
            'answers_by_gender', COALESCE(qs.answers_by_gender, '{}'::jsonb),
            'answers_by_country', COALESCE(qs.answers_by_country, '{}'::jsonb)
        )
        ELSE NULL
    END as statistics
FROM UniqueQuestions uq
JOIN QuestionAndRole qr ON uq.id = qr.id
LEFT JOIN QuestionStats qs ON uq.id = qs.question_id
ORDER BY uq.id DESC;
"""


VOTES_AND_STATISTICS_BY_USER_ID_PAGINATED = """
WITH UserQuestions AS (
    -- Get question IDs and role for the user with proper filtering and pagination
    SELECT 
        q.id AS question_id,
        CASE
            WHEN q.author_id = :user_id THEN 'author'
            ELSE 'respondent'
        END AS role
    FROM questions q
    LEFT JOIN answers a ON q.id = a.question_id AND a.user_id = :user_id
    WHERE (
        (CAST(:role_filter AS TEXT) = 'all' AND (a.user_id = :user_id OR q.author_id = :user_id))
        OR (CAST(:role_filter AS TEXT) = 'author' AND q.author_id = :user_id)
        OR (CAST(:role_filter AS TEXT) = 'respondent' AND a.user_id = :user_id AND q.author_id != :user_id)
    )
    GROUP BY q.id, q.author_id, q.created_at
    ORDER BY q.created_at DESC  -- Use created_at for consistent ordering
    LIMIT :limit OFFSET :offset
),
QuestionVotesAndStats AS (
    SELECT
        uq.question_id,
        uq.role,
        -- Demographics statistics (only for questions where user is author)
        (
            CASE 
                WHEN uq.role = 'author' THEN
                    json_build_object(
                        'age', (
                            SELECT json_agg(json_build_object(
                                'range', age_range, 
                                'count', count,
                                'percentage', percentage
                            ))
                            FROM (
                                SELECT
                                    CASE
                                        WHEN EXTRACT(YEAR FROM AGE(u.birthday)) < 18 THEN 'Under 18'
                                        WHEN EXTRACT(YEAR FROM AGE(u.birthday)) BETWEEN 18 AND 24 THEN '18-24'
                                        WHEN EXTRACT(YEAR FROM AGE(u.birthday)) BETWEEN 25 AND 34 THEN '25-34'
                                        WHEN EXTRACT(YEAR FROM AGE(u.birthday)) BETWEEN 35 AND 44 THEN '35-44'
                                        WHEN EXTRACT(YEAR FROM AGE(u.birthday)) BETWEEN 45 AND 54 THEN '45-54'
                                        WHEN EXTRACT(YEAR FROM AGE(u.birthday)) BETWEEN 55 AND 64 THEN '55-64'
                                        ELSE '65+'
                                    END AS age_range,
                                    COUNT(*) AS count,
                                    ROUND(
                                        (COUNT(*) * 100.0) / 
                                        NULLIF(SUM(COUNT(*)) OVER (), 0), 
                                        2
                                    ) AS percentage
                                FROM answers a3
                                JOIN users u ON a3.user_id = u.id
                                WHERE a3.question_id = uq.question_id AND u.birthday IS NOT NULL
                                GROUP BY 1
                            ) age_stats
                        ),
                        'gender', (
                            SELECT json_agg(json_build_object(
                                'gender', gender, 
                                'count', count,
                                'percentage', percentage
                            ))
                            FROM (
                                SELECT 
                                    u.gender, 
                                    COUNT(*) AS count,
                                    ROUND(
                                        (COUNT(*) * 100.0) / 
                                        NULLIF(SUM(COUNT(*)) OVER (), 0), 
                                        2
                                    ) AS percentage
                                FROM answers a4
                                JOIN users u ON a4.user_id = u.id
                                WHERE a4.question_id = uq.question_id AND u.gender IS NOT NULL
                                GROUP BY u.gender
                            ) gender_stats
                        ),
                        'geo', (
                            SELECT json_agg(json_build_object(
                                'country_id', country_id, 
                                'country_name', country_name, 
                                'count', count,
                                'percentage', percentage
                            ))
                            FROM (
                                SELECT 
                                    c.id AS country_id, 
                                    c.name AS country_name, 
                                    COUNT(*) AS count,
                                    ROUND(
                                        (COUNT(*) * 100.0) / 
                                        NULLIF(SUM(COUNT(*)) OVER (), 0), 
                                        2
                                    ) AS percentage
                                FROM answers a5
                                JOIN users u ON a5.user_id = u.id
                                LEFT JOIN countries c ON u.country_id = c.id
                                WHERE a5.question_id = uq.question_id
                                GROUP BY c.id, c.name
                            ) geo_stats
                        )
                    )
                ELSE NULL  -- No statistics for respondent questions
            END
        ) AS statistics
    FROM UserQuestions uq
)
SELECT 
    question_id AS id,
    role,
    statistics
FROM QuestionVotesAndStats
ORDER BY question_id DESC;  -- Maintain ordering
"""

STATISTICS_BY_QUESTION_IDS_FOR_AUTHOR = """
WITH QuestionRoleAndStats AS (
    SELECT
        q.id AS question_id,
        CASE
            WHEN q.author_id = :user_id THEN 'author'
            ELSE 'respondent'
        END AS role,
        -- Demographics statistics (only for questions where user is author)
        (
            CASE 
                WHEN q.author_id = :user_id THEN
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
                                WHERE a3.question_id = q.id AND u.birthday IS NOT NULL
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
                                WHERE a4.question_id = q.id AND u.gender IS NOT NULL
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
                                WHERE a5.question_id = q.id
                                GROUP BY c.id, c.name
                            ) geo_stats
                        )
                    )
                ELSE NULL  -- No statistics for respondent questions
            END
        ) AS statistics
    FROM questions q
    WHERE q.id = ANY(:question_ids)
)
SELECT 
    question_id AS id,
    role,
    statistics
FROM QuestionRoleAndStats
WHERE question_id = ANY(:question_ids)
ORDER BY question_id;
""" 


STATISTICS_ALL_QUESTION_OPTIONS = """
SELECT
    qo.question_id,
    qo.id AS option_id,
    qo.text AS option_text,
    (
        SELECT COUNT(*)
        FROM answer_options ao
        WHERE ao.option_id = qo.id
    ) AS vote_count,
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
                FROM answers a
                JOIN users u ON a.user_id = u.id
                JOIN answer_options ao ON a.id = ao.answer_id
                WHERE a.question_id = qo.question_id AND ao.option_id = qo.id AND u.birthday IS NOT NULL
                GROUP BY 1
            ) AS age_counts
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
                FROM answers a
                JOIN users u ON a.user_id = u.id
                JOIN answer_options ao ON a.id = ao.answer_id
                WHERE a.question_id = qo.question_id AND ao.option_id = qo.id AND u.gender IS NOT NULL
                GROUP BY u.gender
            ) AS gender_counts
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
                FROM answers a
                JOIN users u ON a.user_id = u.id
                LEFT JOIN countries c ON u.country_id = c.id
                JOIN answer_options ao ON a.id = ao.answer_id
                WHERE a.question_id = qo.question_id AND ao.option_id = qo.id
                GROUP BY c.id, c.name
            ) AS geo_counts
        )
    ) AS statistics
FROM question_options qo
WHERE qo.question_id = :question_id
GROUP BY qo.question_id, qo.id, qo.text;
"""


STATISTICS_SINGLE_QUESTION_OPTION = """
SELECT
    qo.question_id,
    qo.id AS option_id,
    qo.text AS option_text,
    (
        SELECT COUNT(*)
        FROM answer_options ao
        WHERE ao.option_id = :option_id
    ) AS vote_count,
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
                FROM answers a
                JOIN users u ON a.user_id = u.id
                JOIN answer_options ao ON a.id = ao.answer_id
                WHERE ao.option_id = :option_id AND u.birthday IS NOT NULL
                GROUP BY 1
            ) AS age_counts
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
                FROM answers a
                JOIN users u ON a.user_id = u.id
                JOIN answer_options ao ON a.id = ao.answer_id
                WHERE ao.option_id = :option_id AND u.gender IS NOT NULL
                GROUP BY u.gender
            ) AS gender_counts
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
                FROM answers a
                JOIN users u ON a.user_id = u.id
                LEFT JOIN countries c ON u.country_id = c.id
                JOIN answer_options ao ON a.id = ao.answer_id
                WHERE ao.option_id = :option_id
                GROUP BY c.id, c.name
            ) AS geo_counts
        )
    ) AS statistics
FROM question_options qo
WHERE qo.id = :option_id
GROUP BY qo.question_id, qo.id, qo.text;
"""

MUTUALITY = """
-- Step 1: Your favourited hashtags — everything is scoped to these
WITH my_favourite_hashtags AS (
    SELECT subscribed_to_id AS hashtag_id
    FROM subscriptions
    WHERE subscriber_id = :my_id
      AND subscribed_to_type = 'hashtag'
      AND favourite = true
),

-- Step 2: All answers under your favourite hashtags by you or the other user
hashtag_activity AS (
    SELECT
        qhl.hashtag_id,
        a.user_id,
        a.question_id
    FROM answers a
    JOIN question_hashtag_links qhl ON qhl.question_id = a.question_id
    JOIN my_favourite_hashtags fav ON qhl.hashtag_id = fav.hashtag_id
    WHERE a.user_id = :my_id OR a.user_id = :other_id
),

-- Step 3: Your usage count per hashtag
my_usage AS (
    SELECT hashtag_id, COUNT(DISTINCT question_id) AS my_total
    FROM hashtag_activity
    WHERE user_id = :my_id
    GROUP BY hashtag_id
),

-- Step 4: Other user's usage count per hashtag
other_usage AS (
    SELECT hashtag_id, COUNT(DISTINCT question_id) AS other_total
    FROM hashtag_activity
    WHERE user_id = :other_id
    GROUP BY hashtag_id
),

-- Step 5: Shared question count (mutual usage) per hashtag
mutual_usage AS (
    SELECT
        h1.hashtag_id,
        COUNT(DISTINCT h1.question_id) AS common_total
    FROM hashtag_activity h1
    JOIN hashtag_activity h2
        ON h1.hashtag_id = h2.hashtag_id
        AND h1.question_id = h2.question_id
    WHERE h1.user_id = :my_id AND h2.user_id = :other_id
    GROUP BY h1.hashtag_id
)

-- Final: Join stats + metadata, restricted to favourites, ordered by most shared usage
SELECT
    h.id AS hashtag_id,
    h.name AS hashtag_name,
    my.my_total,
    other.other_total,
    COALESCE(mutual.common_total, 0) as common_total,
    mutual.common_total::DECIMAL / NULLIF(my.my_total, 0) AS mutuality
FROM hashtags h
JOIN my_favourite_hashtags fav ON h.id = fav.hashtag_id
LEFT JOIN my_usage my ON h.id = my.hashtag_id
LEFT JOIN other_usage other ON h.id = other.hashtag_id
LEFT JOIN mutual_usage mutual ON h.id = mutual.hashtag_id
WHERE my.my_total IS NOT NULL
ORDER BY mutual.common_total DESC NULLS LAST
LIMIT :limit;
"""


SIMILARITY = """
-- Step 1: Your favourited hashtags only
WITH my_favourite_hashtags AS (
    SELECT subscribed_to_id AS hashtag_id
    FROM subscriptions
    WHERE subscriber_id = :my_id
      AND subscribed_to_type = 'hashtag'
      AND favourite = true
),

-- Step 2: Your answers with selected options
my_answers AS (
    SELECT a.question_id, ao.option_id
    FROM answers a
    JOIN answer_options ao ON ao.answer_id = a.id
    WHERE a.user_id = :my_id
),

-- Step 3: Other user's answers with selected options
other_answers AS (
    SELECT a.question_id, ao.option_id
    FROM answers a
    JOIN answer_options ao ON ao.answer_id = a.id
    WHERE a.user_id = :other_id
),

-- Step 4: Questions both users answered
common_questions AS (
    SELECT DISTINCT u1.question_id
    FROM my_answers u1
    JOIN other_answers u2 ON u1.question_id = u2.question_id
),

-- Step 5: Compute similarity per question
question_similarity AS (
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

-- Step 6: Attach hashtags to questions, but ONLY keep your favourites early
per_question_similarity AS (
    SELECT
        qs.question_id,
        qhl.hashtag_id,
        CASE
            WHEN qs.union_count > 0 THEN qs.intersection_count::DECIMAL / qs.union_count
            ELSE 0
        END AS similarity
    FROM question_similarity qs
    JOIN question_hashtag_links qhl
        ON qhl.question_id = qs.question_id
    JOIN my_favourite_hashtags fav
        ON qhl.hashtag_id = fav.hashtag_id  -- filtering by favourites here
),

-- Step 7: Aggregate per hashtag
hashtag_similarity AS (
    SELECT
        hashtag_id,
        AVG(similarity) AS avg_similarity,
        COUNT(*) AS common_total
    FROM per_question_similarity
    GROUP BY hashtag_id
)

-- Final: Join metadata and return top N
SELECT
    h.id AS hashtag_id,
    h.name AS hashtag_name,
    hs.avg_similarity,
    hs.common_total
FROM hashtag_similarity hs
JOIN hashtags h ON h.id = hs.hashtag_id
ORDER BY hs.common_total DESC NULLS LAST
LIMIT :limit;
"""


MUTUALITY_AND_SIMILARITY = """
-- Step 1: Your favorited hashtags
WITH my_favourite_hashtags AS (
    SELECT subscribed_to_id AS hashtag_id
    FROM subscriptions
    WHERE subscriber_id = :my_id
      AND subscribed_to_type = 'hashtag'
      AND favourite = true
),

-- Step 2: All answers under your favorite hashtags by you or the other user
hashtag_activity AS (
    SELECT
        qhl.hashtag_id,
        a.user_id,
        a.question_id
    FROM answers a
    JOIN question_hashtag_links qhl ON qhl.question_id = a.question_id
    JOIN my_favourite_hashtags fav ON qhl.hashtag_id = fav.hashtag_id
    WHERE a.user_id IN (:my_id, :other_id)
),

-- Step 3: Your usage count per hashtag
my_usage AS (
    SELECT hashtag_id, COUNT(DISTINCT question_id) AS my_total
    FROM hashtag_activity
    WHERE user_id = :my_id
    GROUP BY hashtag_id
),

-- Step 4: Other user's usage count per hashtag
other_usage AS (
    SELECT hashtag_id, COUNT(DISTINCT question_id) AS other_total
    FROM hashtag_activity
    WHERE user_id = :other_id
    GROUP BY hashtag_id
),

-- Step 5: Shared question count (mutual usage) per hashtag
mutual_usage AS (
    SELECT
        h1.hashtag_id,
        COUNT(DISTINCT h1.question_id) AS common_total
    FROM hashtag_activity h1
    JOIN hashtag_activity h2
        ON h1.hashtag_id = h2.hashtag_id
        AND h1.question_id = h2.question_id
    WHERE h1.user_id = :my_id AND h2.user_id = :other_id
    GROUP BY h1.hashtag_id
),

-- Step 6: Your answers with selected options
my_answers AS (
    SELECT a.question_id, ao.option_id
    FROM answers a
    JOIN answer_options ao ON ao.answer_id = a.id
    WHERE a.user_id = :my_id
),

-- Step 7: Other user's answers with selected options
other_answers AS (
    SELECT a.question_id, ao.option_id
    FROM answers a
    JOIN answer_options ao ON ao.answer_id = a.id
    WHERE a.user_id = :other_id
),

-- Step 8: Questions both users answered
common_questions AS (
    SELECT DISTINCT u1.question_id
    FROM my_answers u1
    JOIN other_answers u2 ON u1.question_id = u2.question_id
),

-- Step 9: Compute similarity per question
question_similarity AS (
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

-- Step 10: Attach hashtags to questions, restricted to favorites
per_question_similarity AS (
    SELECT
        qs.question_id,
        qhl.hashtag_id,
        CASE
            WHEN qs.union_count > 0 THEN qs.intersection_count::DECIMAL / qs.union_count
            ELSE 0
        END AS similarity
    FROM question_similarity qs
    JOIN question_hashtag_links qhl ON qhl.question_id = qs.question_id
    JOIN my_favourite_hashtags fav ON qhl.hashtag_id = fav.hashtag_id
),

-- Step 11: Aggregate similarity per hashtag
hashtag_similarity AS (
    SELECT
        hashtag_id,
        AVG(similarity) AS avg_similarity
    FROM per_question_similarity
    GROUP BY hashtag_id
)

-- Final: Join all stats and metadata
SELECT
    h.id AS hashtag_id,
    h.name AS hashtag_name,
    COALESCE(my.my_total, 0) AS my_total,
    COALESCE(other.other_total, 0) AS other_total,
    COALESCE(mutual.common_total, 0) AS common_total,
    COALESCE(mutual.common_total::DECIMAL / NULLIF(my.my_total, 0), 0) AS mutuality,
    COALESCE(hs.avg_similarity, 0) AS avg_similarity
FROM hashtags h
JOIN my_favourite_hashtags fav ON h.id = fav.hashtag_id
LEFT JOIN my_usage my ON h.id = my.hashtag_id
LEFT JOIN other_usage other ON h.id = other.hashtag_id
LEFT JOIN mutual_usage mutual ON h.id = mutual.hashtag_id
LEFT JOIN hashtag_similarity hs ON h.id = hs.hashtag_id
WHERE my.my_total IS NOT NULL
ORDER BY mutual.common_total DESC NULLS LAST
LIMIT :limit;
"""

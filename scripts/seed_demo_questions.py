#!/usr/bin/env python3
"""Seeds demo questions from demo_questions.json as author=vece user."""
import json
import os
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
env_path = project_root / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ[k.strip()] = v.strip().strip('"').strip("'")


def main():
    import psycopg2
    from datetime import datetime

    host = os.getenv("POSTGRES_HOST")
    port = 5432 if host and "pooler" in host else int(os.getenv("POSTGRES_PORT", "5432"))
    conn = psycopg2.connect(
        host=host,
        port=port,
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        dbname=os.getenv("POSTGRES_DB"),
    )
    conn.autocommit = False
    cur = conn.cursor()

    # Get vece user id
    cur.execute("SELECT id FROM users WHERE username = 'vece'")
    row = cur.fetchone()
    if not row:
        print("vece user not found. Run scripts/create_vece_user.sh first.")
        conn.close()
        return 1

    author_id = row[0]

    # Delete existing demo questions from vece (idempotent re-run)
    cur.execute("DELETE FROM questions WHERE author_id = %s", (author_id,))

    # Load all hashtags: name -> id
    cur.execute("SELECT id, name FROM hashtags")
    hashtag_by_name = {r[1]: r[0] for r in cur.fetchall()}

    # Load questions
    json_path = project_root / "scripts" / "demo_questions.json"
    if not json_path.exists():
        print(f"File not found: {json_path}")
        return 1

    questions = json.loads(json_path.read_text())
    active_till = datetime(2027, 12, 31, 23, 59, 59)

    inserted = 0
    for q in questions:
        text = q["text"]
        max_options = int(q["max_options"])
        allow_user_options = bool(q.get("allow_user_options", False))
        options = q.get("options", [])
        hashtags = q.get("hashtags", [])

        # Parse active_till if string
        at = q.get("active_till", "2027-12-31T23:59:59Z")
        if isinstance(at, str):
            active_till = datetime.fromisoformat(at.replace("Z", "+00:00")).replace(tzinfo=None)

        cur.execute(
            """
            INSERT INTO questions (author_id, text, max_options, active_till, allow_user_options)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
            """,
            (author_id, text, max_options, active_till, allow_user_options),
        )
        question_id = cur.fetchone()[0]

        for i, opt in enumerate(sorted(options, key=lambda x: x.get("position", 0))):
            pos = opt.get("position", i)  # fallback to index if position missing
            cur.execute(
                """
                INSERT INTO question_options (question_id, text, position, author_id, by_question_author)
                VALUES (%s, %s, %s, %s, TRUE)
                """,
                (question_id, opt["text"], pos, author_id),
            )

        for tag_name in hashtags:
            if tag_name in hashtag_by_name:
                hashtag_id = hashtag_by_name[tag_name]
                cur.execute(
                    """
                    INSERT INTO question_hashtag_links (question_id, hashtag_id)
                    VALUES (%s, %s)
                    ON CONFLICT (question_id, hashtag_id) DO NOTHING
                    """,
                    (question_id, hashtag_id),
                )

        inserted += 1

    conn.commit()
    conn.close()
    print(f"Inserted {inserted} demo questions from vece user.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

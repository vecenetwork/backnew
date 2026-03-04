#!/usr/bin/env python3
"""Clears all questions and hashtags from the database. Run before seeding new tags and questions."""
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

    # 1. Delete subscriptions to hashtags (orphaned refs)
    cur.execute("DELETE FROM subscriptions WHERE subscribed_to_type = 'hashtag'")
    subs_deleted = cur.rowcount

    # 2. Truncate questions (CASCADE removes question_options, question_hashtag_links, answers, answer_options)
    cur.execute("TRUNCATE TABLE questions CASCADE")
    conn.commit()

    # 3. Truncate hashtags
    cur.execute("TRUNCATE TABLE hashtags CASCADE")
    conn.commit()

    conn.close()
    print(f"✅ Cleared: {subs_deleted} hashtag subscriptions, all questions, all hashtags.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Creates or updates VECE user (username: vece, password: testpass123). Sets is_verified=True, is_active=True."""
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


# bcrypt hash for "testpass123"
PASSWORD_HASH = "$2b$12$pAzELgYyuJfxGI1KeU038uQzBk5KyNFeX08eBabOPL0aUkRyWIPjS"


def main():
    import psycopg2

    # Same port logic as run_migrations: 5432 for Supabase pooler
    host = os.getenv("POSTGRES_HOST")
    port = 5432 if host and "pooler" in host else int(os.getenv("POSTGRES_PORT", "5432"))
    conn = psycopg2.connect(
        host=host,
        port=port,
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        dbname=os.getenv("POSTGRES_DB"),
    )
    conn.autocommit = True
    cur = conn.cursor()

    # Get first country (ensure at least one exists)
    cur.execute("SELECT id FROM countries LIMIT 1")
    row = cur.fetchone()
    if not row:
        cur.execute(
            """
            INSERT INTO countries (id, code, name, full_name, iso3, number, continent_code, display_order)
            VALUES (1, 'US', 'United States of America', 'United States of America', 'USA', '840', 'NA', 1)
            ON CONFLICT (id) DO NOTHING
            """
        )
        cur.execute("SELECT id FROM countries LIMIT 1")
        row = cur.fetchone()
    if not row:
        print("No countries in DB. Run migrations first.")
        conn.close()
        return 1

    country_id = row[0]

    # Check if vece exists
    cur.execute("SELECT id, is_verified, is_active FROM users WHERE username = 'vece'")
    existing = cur.fetchone()

    if existing:
        user_id, is_verified, is_active = existing
        if not is_verified or not is_active:
            cur.execute(
                "UPDATE users SET is_verified = TRUE, is_active = TRUE WHERE username = 'vece'"
            )
            print("Updated vece user (is_verified=True, is_active=True)")
        else:
            print("vece user already exists and is active")
    else:
        cur.execute(
            """
            INSERT INTO users (
                name, surname, username, email, password_hash, birthday,
                country_id, gender, is_verified, is_active, role
            ) VALUES (
                'VECE', 'Official', 'vece', 'vece@vece.ai', %s, '1990-01-01',
                %s, 'Other', TRUE, TRUE, 'user'
            )
            RETURNING id
            """,
            (PASSWORD_HASH, country_id),
        )
        user_id = cur.fetchone()[0]
        cur.execute(
            """
            INSERT INTO user_settings (user_id, show_name_option, show_question_results)
            VALUES (%s, 'Name', 'All')
            """,
            (user_id,),
        )
        print("Created vece user (username: vece, password: testpass123)")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())

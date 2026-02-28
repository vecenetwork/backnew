#!/usr/bin/env python3
"""Creates tester user: email kolievpapel@gmail.com, username tester, password Testtest1."""
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

# bcrypt hash for "Testtest1"
PASSWORD_HASH = "$2b$12$T2AwOVgY4pO7e/04z/WiD.his5whTpuZXWOekZ1UwIt.NqYkpL6xK"


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
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("SELECT id FROM countries LIMIT 1")
    row = cur.fetchone()
    if not row:
        print("No countries in DB. Run migrations first.")
        conn.close()
        return 1
    country_id = row[0]

    cur.execute(
        "SELECT id FROM users WHERE username = 'tester' OR email = 'kolievpapel@gmail.com'"
    )
    existing = cur.fetchone()
    if existing:
        cur.execute(
            """
            UPDATE users SET password_hash = %s, is_verified = TRUE, is_active = TRUE
            WHERE id = %s
            """,
            (PASSWORD_HASH, existing[0]),
        )
        print("Updated tester user (password reset to Testtest1)")
    else:
        cur.execute(
            """
            INSERT INTO users (
                name, surname, username, email, password_hash, birthday,
                country_id, gender, is_verified, is_active, role
            ) VALUES (
                'Tester', 'User', 'tester', 'kolievpapel@gmail.com', %s, '1990-01-01',
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
        print("Created tester user (username: tester, email: kolievpapel@gmail.com, password: Testtest1)")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())

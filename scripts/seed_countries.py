#!/usr/bin/env python3
"""
Seeds the countries table with all 246 countries.
Use when the table exists but has partial/wrong data (e.g. only USA at id=1).

Run: python3 scripts/seed_countries.py

Requires .env with: POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB

Handles: renames existing USA row, inserts full list, updates user references.
"""
import os
import sys
from pathlib import Path

# Load .env from project root
project_root = Path(__file__).parent.parent
env_path = project_root / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ[key.strip()] = value.strip().strip('"').strip("'")

# Use the full seed migration (handles existing partial data)
COUNTRIES_SQL = project_root / "liquibase/changelog/sql/v/2026-03-03/01_seed_countries_full.sql"


def seed_countries():
    import psycopg2

    host = os.getenv("POSTGRES_HOST")
    port = int(os.getenv("POSTGRES_PORT", "5432"))
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    database = os.getenv("POSTGRES_DB")

    if host and "pooler" in host:
        port = 5432

    if not all([host, user, password, database]):
        print("❌ Set POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB in .env")
        return False

    if not COUNTRIES_SQL.exists():
        print(f"❌ File not found: {COUNTRIES_SQL}")
        return False

    sql = COUNTRIES_SQL.read_text()
    # Skip comments
    sql = "\n".join(
        line for line in sql.splitlines()
        if not line.strip().startswith("--")
    )
    statements = [
        (s.strip() + ";").strip()
        for s in sql.split(";")
        if s.strip() and (s.strip() + ";").strip() != ";"
    ]

    conn = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        dbname=database,
    )
    conn.autocommit = True

    try:
        for stmt in statements:
            if not stmt or stmt.startswith("--"):
                continue
            try:
                with conn.cursor() as cur:
                    cur.execute(stmt)
            except psycopg2.Error as e:
                err_msg = str(e).lower()
                if "already exists" in err_msg:
                    # Table exists, continue to INSERT
                    pass
                else:
                    print(f"❌ Error: {e}")
                    raise

        # Verify count
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM countries")
            count = cur.fetchone()[0]
        if count < 200:
            print(f"⚠️  Only {count} countries in DB. Expected 246. Check for errors above.")
        else:
            print(f"✅ Countries seeded. Total: {count}")
        return True
    finally:
        conn.close()


if __name__ == "__main__":
    try:
        ok = seed_countries()
        sys.exit(0 if ok else 1)
    except Exception as e:
        print(f"\n❌ Failed: {e}")
        sys.exit(1)

#!/usr/bin/env python3
"""Вставляет хештеги в таблицу hashtags (если пусто)."""
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
    conn.autocommit = True

    sql_file = project_root / "liquibase/changelog/sql/v/2025-08-20/01_new_hashtags.sql"
    sql = sql_file.read_text()
    sql = "\n".join(
        l for l in sql.splitlines()
        if not l.strip().startswith("--liquibase") and not l.strip().startswith("--changeset")
    )
    # Исправляем ON CONFLICT для PostgreSQL
    sql = sql.replace("ON CONFLICT DO NOTHING", "ON CONFLICT (name) DO NOTHING")

    cur = conn.cursor()
    cur.execute(sql)
    count = cur.rowcount
    conn.close()

    print(f"✅ Добавлено хештегов: {count}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

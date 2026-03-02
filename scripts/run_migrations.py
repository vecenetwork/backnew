#!/usr/bin/env python3
"""
Применяет все SQL-миграции к базе Supabase.
Запуск: python scripts/run_migrations.py
"""
import os
import sys
from pathlib import Path

# Загружаем .env из корня проекта
project_root = Path(__file__).parent.parent
env_path = project_root / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ[key.strip()] = value.strip().strip('"').strip("'")

# Порядок миграций (как в Liquibase)
MIGRATION_FILES = [
    "liquibase/changelog/sql/v/2025-02-25/00_countries.sql",
    "liquibase/changelog/sql/v/2025-02-25/01_barrier.sql",
    "liquibase/changelog/sql/v/2025-02-25/02_user_data.sql",
    "liquibase/changelog/sql/v/2025-02-25/03_hashtags.sql",
    "liquibase/changelog/sql/v/2025-02-25/04_subscriptions.sql",
    "liquibase/changelog/sql/v/2025-02-25/06_question_answers.sql",
    "liquibase/changelog/sql/v/2025-02-25/07_waitlist.sql",
    "liquibase/changelog/sql/v/2025-06-06/01_rename_author_to_author_id.sql",
    "liquibase/changelog/sql/v/2025-06-08/01_add_total_answers_to_questions.sql",
    "liquibase/changelog/sql/v/2025-06-08/02_add_stats_to_options_and_update.sql",
    "liquibase/changelog/sql/v/2025-08-20/01_new_hashtags.sql",
    "liquibase/changelog/sql/v/2025-10-28/01_add_social_link_to_users.sql",
    "liquibase/changelog/sql/v/2026-03-02/01_pending_registrations.sql",
]


def run_migrations():
    import psycopg2

    host = os.getenv("POSTGRES_HOST")
    port = int(os.getenv("POSTGRES_PORT", "5432"))
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    database = os.getenv("POSTGRES_DB")

    # Для миграций используем session mode (5432) с pooler
    if host and "pooler" in host:
        port = 5432

    if not all([host, user, password, database]):
        print("❌ Не все переменные из .env заданы")
        return False

    conn = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        dbname=database,
    )
    conn.autocommit = True  # каждый execute сразу коммитится

    try:
        for rel_path in MIGRATION_FILES:
            file_path = project_root / rel_path
            if not file_path.exists():
                print(f"⚠️  Файл не найден: {rel_path}")
                continue

            sql = file_path.read_text()
            sql = "\n".join(
                line for line in sql.splitlines()
                if not line.strip().startswith("--liquibase")
                and not line.strip().startswith("--changeset")
            )
            statements = [
                (s.strip() + ";").strip()
                for s in sql.split(";")
                if s.strip() and (s.strip() + ";").strip() != ";"
            ]

            # Весь файл в одной транзакции (важно для CREATE TYPE + CREATE TABLE)
            for stmt in statements:
                if not stmt or stmt.startswith("--"):
                    continue
                try:
                    with conn.cursor() as cur:
                        cur.execute(stmt)
                except psycopg2.Error as e:
                    err_msg = str(e).lower()
                    if any(x in err_msg for x in ("already exists", "duplicate", "does not exist")):
                        pass  # уже применено или колонка переименована
                    else:
                        print(f"❌ Ошибка в {rel_path}: {e}")
                        raise
            print(f"✅ {rel_path}")

        print("\n✅ Все миграции применены успешно!")
        return True
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    try:
        ok = run_migrations()
        sys.exit(0 if ok else 1)
    except Exception as e:
        print(f"\n❌ Миграция прервана: {e}")
        sys.exit(1)

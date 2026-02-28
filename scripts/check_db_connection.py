#!/usr/bin/env python3
"""Проверка подключения к Supabase PostgreSQL."""
import os
import sys
from pathlib import Path

# Загружаем .env из корня проекта
env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ[key.strip()] = value.strip().strip('"').strip("'")

async def test():
    import asyncpg

    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT", "5432")
    user = os.getenv("POSTGRES_USER")
    db = os.getenv("POSTGRES_DB")
    if not all([host, user, db]):
        print("❌ Не все переменные из .env загружены. Убедитесь, что .env в папке vecenetwork-project-main.")
        return False

    try:
        conn = await asyncpg.connect(
            host=host,
            port=int(port),
            user=user,
            password=os.getenv("POSTGRES_PASSWORD"),
            database=db,
        )
        await conn.close()
        print("✅ Подключение успешно! Пароль правильный, база доступна.")
        return True
    except Exception as e:
        err = str(e)
        if "nodename nor servname" in err or "getaddrinfo" in err.lower():
            print("❌ Не удаётся найти сервер Supabase. Возможные причины:")
            print("   • Проект приостановлен (Supabase останавливает неактивные проекты)")
            print("   • Неверная строка подключения — возьмите новую в Supabase: Connect → URI")
            print("   • Нет интернета")
        else:
            print(f"❌ Ошибка подключения: {e}")
        return False

if __name__ == "__main__":
    import asyncio
    ok = asyncio.run(test())
    sys.exit(0 if ok else 1)

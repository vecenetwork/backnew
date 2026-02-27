# Изменения в миграциях (проверка и исправления)

## Что было проверено и исправлено

### 1. `00_countries.sql`
- **Проблема:** INSERT без ON CONFLICT — при повторном запуске падал с ошибкой duplicate key.
- **Исправление:** Добавлено `ON CONFLICT (id) DO NOTHING` — миграция стала идемпотентной.

### 2. `01_new_hashtags.sql`
- **Проблема:** `ON CONFLICT DO NOTHING` без указания колонки — в PostgreSQL 15 требуется `ON CONFLICT (column) DO NOTHING`.
- **Исправление:** Заменено на `ON CONFLICT (name) DO NOTHING`.

### 3. `01_add_total_answers_to_questions.sql`
- **Проблема:** При повторном запуске `ADD COLUMN` падал с "column already exists".
- **Исправление:** Добавлено `IF NOT EXISTS` — `ADD COLUMN IF NOT EXISTS`.

### 4. `02_add_stats_to_options_and_update.sql`
- **Проблема:** Аналогично — колонки count и percentage уже могли существовать.
- **Исправление:** Добавлено `IF NOT EXISTS` для обеих колонок.

### 5. `01_add_social_link_to_users.sql`
- **Проблема:** `ADD COLUMN social_link` падал при повторном запуске.
- **Исправление:** Добавлено `IF NOT EXISTS`.

### 6. `run_migrations.py`
- **Дополнение:** В список игнорируемых ошибок добавлено `"does not exist"` — для случая, когда колонка `author` уже переименована в `author_id` (миграция 2025-06-06).

## Миграции без изменений (проверены)

- `01_barrier.sql` — CREATE TABLE, корректен.
- `02_user_data.sql` — CREATE TYPE, CREATE TABLE, корректен.
- `03_hashtags.sql` — CREATE TABLE, корректен.
- `04_subscriptions.sql` — CREATE TABLE, CHECK, индексы — корректен.
- `06_question_answers.sql` — CREATE TABLE, корректен.
- `07_waitlist.sql` — CREATE TABLE, корректен.
- `01_rename_author_to_author_id.sql` — ALTER RENAME, корректен (ошибка "does not exist" обрабатывается скриптом).

## Результат

Все миграции успешно применяются при повторном запуске. Скрипт `run_migrations.py` можно запускать многократно без ошибок.

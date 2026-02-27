# Деплой бэкенда на Railway

## Шаг 1: Репозиторий на GitHub

1. Создай репозиторий на GitHub (если ещё нет).
2. Залей код:
   ```bash
   cd /Users/ilya/Desktop/back\ copy/vecenetwork-project-main
   git init
   git add .
   git commit -m "Initial"
   git remote add origin https://github.com/ТВОЙ_ЮЗЕРНЕЙМ/vecenetwork.git
   git push -u origin main
   ```

## Шаг 2: Создать проект в Railway

1. Зайди на [railway.app](https://railway.app) → **New Project**.
2. Выбери **Deploy from GitHub repo**.
3. Подключи GitHub и выбери репозиторий `vecenetwork-project-main`.

## Шаг 3: Настроить сервис

1. Railway создаст сервис.
2. В **Settings** → **Root Directory** укажи: `backend` (чтобы контекст сборки был в папке backend).
3. Railway найдёт и использует `backend/Dockerfile`.

## Шаг 4: Переменные окружения

В Railway: **Variables** → добавь переменные (значения из `.env`):

| Переменная | Значение |
|------------|----------|
| `POSTGRES_HOST` | aws-1-us-east-2.pooler.supabase.com |
| `POSTGRES_PORT` | 6543 |
| `POSTGRES_USER` | postgres.wwjpxolnmiqmtudwojng |
| `POSTGRES_PASSWORD` | Askanswerandcompare2025! |
| `POSTGRES_DB` | postgres |
| `BASE_URL` | https://ТВОЙ-ДОМЕН.railway.app/api |
| `FRONTEND_URL` | https://твой-фронт.vercel.app (или где хостится фронт) |
| `GOOGLE_API_KEY` | AIzaSyA-Xy16R8OssUIpXBZngIqap6kjgK9GjKo |
| `EMAIL_ADDRESS` | info@vece.ai |
| `EMAIL_PASSWORD` | (если есть — пароль для SMTP) |

**Важно:** `BASE_URL` и `FRONTEND_URL` задай **после** того, как Railway выдаст домен.

## Шаг 5: Публичный URL

1. В **Settings** → **Networking** → **Generate Domain**.
2. Railway выдаст URL вида `vecenetwork-production-xxxx.up.railway.app`.
3. Обнови **Variables**:
   - `BASE_URL` = `https://vecenetwork-production-xxxx.up.railway.app/api`
   - `FRONTEND_URL` = URL твоего фронта (Vercel и т.п.)

## Шаг 6: URL API

API будет доступно по адресу:
```
https://ТВОЙ-ДОМЕН.railway.app/api
```

Проверка: `https://ТВОЙ-ДОМЕН.railway.app/api/health`

## Шаг 7: Фронт

В `.env` или `.env.production` на фронте:
```
VITE_API_BASE_URL=https://ТВОЙ-ДОМЕН.railway.app/api
```

---

**Кратко:** только бэк на Railway. БД — Supabase (уже настроена). Фронт — отдельно (Vercel, Netlify и т.д.).

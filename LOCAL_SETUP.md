# Локальная настройка: БД, бэк, фронт, Sign Up

## Связки

| Компонент | Настройка | Статус |
|-----------|-----------|--------|
| **БД** | Supabase PostgreSQL (`.env`: POSTGRES_*) | ✅ Подключена |
| **Бэк** | `http://localhost:8000`, префикс `/api` | ✅ |
| **Фронт** | `http://localhost:3000`, `.env.local` → `VITE_API_BASE_URL=http://localhost:8000/api` | ✅ |

## Sign Up (регистрация)

1. **Шаг 1:** Пользователь вводит email → `POST /api/register/request-email`
2. **Письмо:** Ссылка вида `http://localhost:8000/api/verify-email?token=xxx`
3. **Клик по ссылке:** Бэк проверяет токен и редиректит на `http://localhost:3000/sign-up?email=xxx&token=xxx`
4. **Шаг 2:** Пользователь вводит username и password → `POST /api/register/complete`

## Email (отправка писем)

### Текущая конфигурация (`.env`)

- `EMAIL_ADDRESS=info@vece.ai`
- `EMAIL_PASSWORD=` — **пусто**

### Поведение

- **Если `EMAIL_PASSWORD` пустой:** ссылка активации выводится в консоль бэка (для локальной разработки).
- **Если `EMAIL_PASSWORD` задан:** письма отправляются через SMTP (Gmail: `smtp.gmail.com:587`).

### Для реальной отправки писем

1. **Gmail:** создать App Password и указать в `.env`:
   ```
   EMAIL_ADDRESS=your@gmail.com
   EMAIL_PASSWORD=xxxx xxxx xxxx xxxx
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   ```

2. **Домен vece.ai:** настроить SMTP для `info@vece.ai` и указать хост/порт/пароль в `.env`.

## Шаблон письма

Используется `VERIFY_EMAIL_TEMPLATE` в `backend/src/app/services/email/verification.py` — HTML-письмо с кнопкой «Verify Email Address».

## Запуск

```bash
# Терминал 1 — бэк
cd vecenetwork-project-main
./scripts/run_app.sh

# Терминал 2 — фронт
cd front\ copy
npm run dev
```

При пустом `EMAIL_PASSWORD` после ввода email смотри консоль бэка — там будет ссылка для активации.

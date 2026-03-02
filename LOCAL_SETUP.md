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
4. **Шаг 2:** Пользователь вводит country, birthday, gender и password → `POST /api/register/complete` (username генерируется автоматически)

## Email (отправка писем)

### Текущая конфигурация (`.env`)

- `EMAIL_ADDRESS=info@vece.ai` — адрес отправителя (должен быть верифицирован в Resend)
- `RESEND_API_KEY=` — **пусто** для локальной разработки

### Поведение

- **Если `RESEND_API_KEY` пустой:** ссылка активации выводится в консоль бэка (для локальной разработки).
- **Если `RESEND_API_KEY` задан:** письма отправляются через [Resend API](https://resend.com).

### Для реальной отправки писем

1. Зарегистрируйся на [Resend](https://resend.com).
2. Добавь и верифицируй домен (например, vece.ai).
3. Создай API ключ и укажи в `.env`:
   ```
   RESEND_API_KEY=re_xxxxxxxx
   EMAIL_ADDRESS=info@vece.ai
   ```

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

При пустом `RESEND_API_KEY` после ввода email смотри консоль бэка — там будет ссылка для активации.

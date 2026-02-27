#!/bin/bash
# Запуск фронта и бэка параллельно (локальная разработка)
# Фронт использует .env.local → http://localhost:8000/api

set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FRONT_DIR="$(dirname "$ROOT")/../front copy"

if [ ! -d "$FRONT_DIR" ]; then
  echo "Frontend not found at: $FRONT_DIR"
  echo "Expected: front copy next to back copy on Desktop"
  exit 1
fi

# Запуск бэка в фоне
echo "Starting backend on http://localhost:8000 ..."
"$ROOT/scripts/run_app.sh" &
BACKEND_PID=$!

# Ждём, пока бэк поднимется
sleep 3
if ! kill -0 $BACKEND_PID 2>/dev/null; then
  echo "Backend failed to start"
  exit 1
fi

# При Ctrl+C убиваем бэк
trap "kill $BACKEND_PID 2>/dev/null || true" EXIT

# Запуск фронта
echo "Starting frontend (uses VITE_API_BASE_URL from .env.local)..."
cd "$FRONT_DIR"
npm run dev

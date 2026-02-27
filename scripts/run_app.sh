#!/bin/bash
# Запуск приложения VECE
# Требуется: Python 3.12+, зависимости установлены (uv sync или pip install -e .)

cd "$(dirname "$0")/.."
export PYTHONPATH="${PWD}/backend/src:${PYTHONPATH}"

# Загружаем .env
if [ -f .env ]; then
  set -a
  source .env
  set +a
fi

cd backend/src
PYTHON="${PWD}/../.venv/bin/python"
[ -x "$PYTHON" ] || PYTHON="$(command -v python3 python 2>/dev/null | head -1)"
exec "$PYTHON" -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

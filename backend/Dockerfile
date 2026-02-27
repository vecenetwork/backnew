FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /src

COPY pyproject.toml uv.lock ./
COPY ./src ./
RUN mkdir -p /src/models

RUN uv sync --frozen --no-cache

EXPOSE 8000
CMD ["sh", "-c", "exec /src/.venv/bin/uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]

import logging
from pathlib import Path

# Загружаем .env из корня проекта (рядом с backend/)
_env_path = Path(__file__).resolve().parent.parent.parent / ".env"
if _env_path.exists():
    from dotenv import load_dotenv
    load_dotenv(_env_path)

from fastapi import FastAPI

from infrastructure.lifespan import lifespan
from infrastructure.middleware.register import register_middleware
from infrastructure.routes import register_routes

logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

app = FastAPI(lifespan=lifespan, root_path="/api")
register_routes(app)
register_middleware(app)


@app.get("/api/health")
def health():
    """Проверка: бэк запущен и доступен по /api."""
    return {"status": "ok", "message": "Backend is running"}

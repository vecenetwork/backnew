import logging
import os
from pathlib import Path

# Загружаем .env из корня проекта (рядом с backend/)
_env_path = Path(__file__).resolve().parent.parent.parent / ".env"
if _env_path.exists():
    from dotenv import load_dotenv  # noqa: E402
    load_dotenv(_env_path)

from fastapi import FastAPI  # noqa: E402
from fastapi.responses import RedirectResponse  # noqa: E402
from infrastructure.lifespan import lifespan  # noqa: E402
from infrastructure.middleware.register import register_middleware  # noqa: E402
from infrastructure.routes import register_routes  # noqa: E402

logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

app = FastAPI(lifespan=lifespan, root_path="/api")
register_routes(app)
register_middleware(app)


@app.get("/")
def root():
    """Редирект с корня на /api/health."""
    return RedirectResponse(url="/api/health", status_code=302)


@app.get("/api/health")
def health():
    """Проверка: бэк запущен и доступен по /api."""
    email_configured = bool(os.getenv("EMAIL_PASSWORD", "").strip())
    base_url = os.getenv("BASE_URL", "http://localhost:8000/api")
    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
    return {
        "status": "ok",
        "message": "Backend is running",
        "email_configured": email_configured,
        "base_url": base_url,
        "frontend_url": frontend_url,
    }

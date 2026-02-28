import os
from typing import TYPE_CHECKING

from starlette.middleware.cors import CORSMiddleware

from infrastructure.middleware.services.logging_middleware import LoggingMiddleware

if TYPE_CHECKING:
    from fastapi import FastAPI


def _get_cors_config() -> dict:
    """Build CORS config from FRONTEND_URL and CORS_ORIGINS."""
    origins: list[str] = []
    frontend = os.getenv("FRONTEND_URL", "http://localhost:3000").rstrip("/")
    if frontend:
        origins.append(frontend)
    extra = os.getenv("CORS_ORIGINS", "")
    for o in extra.split(","):
        o = o.strip().rstrip("/")
        if o and o not in origins:
            origins.append(o)
    if not origins:
        return {"allow_origins": ["*"], "allow_credentials": False}
    return {
        "allow_origins": origins,
        "allow_origin_regex": r"https://.*\.vercel\.app",  # Preview deployments
        "allow_credentials": True,
        "allow_methods": ["*"],
        "allow_headers": ["*"],
        "expose_headers": ["*"],
    }


def register_middleware(app: "FastAPI"):
    """Register all middleware with the FastAPI application."""
    cors_config = _get_cors_config()
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(CORSMiddleware, **cors_config)

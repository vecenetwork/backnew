import os
from typing import TYPE_CHECKING

from starlette.middleware.cors import CORSMiddleware
from starlette.types import ASGIApp

from infrastructure.middleware.services.logging_middleware import LoggingMiddleware

if TYPE_CHECKING:
    from fastapi import FastAPI


def _get_cors_origins() -> tuple[list[str], bool]:
    """Build CORS origins from FRONTEND_URL and CORS_ORIGINS. Returns (origins, use_credentials)."""
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
        return ["*"], False  # Wildcard requires allow_credentials=False
    return origins, True


class CORSAllowVercelMiddleware:
    """Allow CORS from any *.vercel.app origin (for preview deployments)."""

    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: dict, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        origin = None
        for h, v in scope.get("headers", []):
            if h == b"origin":
                origin = v.decode("utf-8")
                break

        async def send_wrapper(message):
            if origin and origin.endswith(".vercel.app") and message.get("type") == "http.response.start":
                headers = list(message.get("headers", []))
                has_acao = any(h == b"access-control-allow-origin" for h, _ in headers)
                if not has_acao:
                    headers.append((b"access-control-allow-origin", origin.encode()))
                    headers.append((b"access-control-allow-credentials", b"true"))
                    headers.append((b"access-control-allow-methods", b"*"))
                    headers.append((b"access-control-allow-headers", b"*"))
                    message = {**message, "headers": headers}
            await send(message)

        if scope["method"] == "OPTIONS" and origin and origin.endswith(".vercel.app"):
            await send(
                {
                    "type": "http.response.start",
                    "status": 200,
                    "headers": [
                        (b"access-control-allow-origin", origin.encode()),
                        (b"access-control-allow-credentials", b"true"),
                        (b"access-control-allow-methods", b"GET, POST, PUT, DELETE, OPTIONS"),
                        (b"access-control-allow-headers", b"*"),
                        (b"access-control-max-age", b"86400"),
                        (b"content-length", b"0"),
                    ],
                }
            )
            await send({"type": "http.response.body", "body": b""})
            return

        await self.app(scope, receive, send_wrapper)


def register_middleware(app: "FastAPI"):
    """Register all middleware with the FastAPI application. CORSAllowVercelMiddleware runs first to handle *.vercel.app."""
    origins, allow_creds = _get_cors_origins()
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=allow_creds,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )
    app.add_middleware(CORSAllowVercelMiddleware)  # Outermost: handles OPTIONS for *.vercel.app

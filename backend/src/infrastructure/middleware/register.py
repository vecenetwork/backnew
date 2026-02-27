from typing import TYPE_CHECKING

from starlette.middleware.cors import CORSMiddleware
from infrastructure.middleware.services.logging_middleware import LoggingMiddleware

if TYPE_CHECKING:
    from fastapi import FastAPI


def register_middleware(app: "FastAPI"):
    """Register all middleware with the FastAPI application"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows specific origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
        allow_headers=["*"],  # Allows all headers
    )
    app.add_middleware(LoggingMiddleware)

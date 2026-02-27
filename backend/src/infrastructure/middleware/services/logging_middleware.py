import time
import json
import logging
from typing import Optional, Any
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse
from starlette.types import ASGIApp

logger = logging.getLogger(__name__)


EXCLUDE_PATH: list[str] = ["/upload-profile-picture", "/docs", "/openapi.json"]
STANDARD_HEADERS = {
    "host",
    "connection",
    "accept",
    "accept-encoding",
    "accept-language",
    "user-agent",
    "sec-fetch-site",
    "sec-fetch-mode",
    "sec-fetch-dest",
    "upgrade-insecure-requests",
}
SENSITIVE_KEYS = {"password", "secret", "token", "key", "auth"}


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        exclude_paths: Optional[list[str]] = None,
        exclude_headers: Optional[set[str]] = None,
        max_body_length: int = 200,
    ):
        super().__init__(app)
        self.exclude_paths = exclude_paths or EXCLUDE_PATH
        self.exclude_headers = exclude_headers or STANDARD_HEADERS
        self.max_body_length = max_body_length

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Skip logging for excluded paths
        request_url = str(request.url)
        if any(excluded in request_url for excluded in self.exclude_paths):
            return await call_next(request)

        # Log request data
        request_body = await self._get_request_body(request)
        sanitized_headers = self._sanitize_headers(
            self._filter_headers(dict(request.headers))
        )
        sanitized_request_body = self._sanitize_body(request_body)
        request_data = {
            "method": request.method,
            "url": request_url,
            "headers": sanitized_headers,
            "body": sanitized_request_body,
        }
        logger.info(f"Request: {json.dumps(request_data, indent=2, default=str)}")

        # Process request and capture response
        response = await call_next(request)
        response_body_log = await self._get_response_body(response)
        if (
            response_body_log
            and isinstance(response_body_log, str)
            and len(response_body_log) > self.max_body_length
        ):
            response_body_log = f"{response_body_log[: self.max_body_length]}..."
        # Log response data
        response_data = {
            "status_code": response.status_code,
            "headers": self._sanitize_headers(dict(response.headers)),
            "body": response_body_log,
            "duration": time.time() - start_time,
        }
        logger.info(f"Response: {json.dumps(response_data, indent=2, default=str)}")

        # Return the original response
        return response

    async def _get_request_body(self, request: Request) -> Optional[str]:
        """Safely extract and decode request body."""
        try:
            body = await request.body()
            return body.decode("utf-8") if body else None
        except UnicodeDecodeError:
            logger.warning(
                "<LoggingMiddleware> Request body could not be decoded as UTF-8"
            )
            return "<non-utf8-body>"
        except Exception as e:
            logger.error(f"<LoggingMiddleware> Error reading request body: {e}")
            return None

    async def _get_response_body(self, response: Response) -> Optional[str]:
        """Safely extract and decode response body (sample for streaming)."""
        if isinstance(response, StreamingResponse):
            try:
                return "<streaming response>"
                # Optional: Log a few initial chunks (commented out to avoid potential issues)
                # chunks: list[bytes] = []
                # async for i, chunk in enumerate(response.body_iterator):
                #     if i < 5:  # Log first 5 chunks
                #         if isinstance(chunk, str):
                #             chunks.append(chunk.encode('utf-8'))
                #         elif isinstance(chunk, (bytes, memoryview)):
                #             chunks.append(bytes(chunk))
                #         else:
                #             logger.warning(f"Unexpected chunk type: {type(chunk)}")
                #     yield chunk  # This would be needed if you were still trying to reconstruct
                # if chunks:
                #     return b"".join(chunks).decode("utf-8", errors="ignore") + "..."
                # else:
                #     return "<empty streaming response>"
            except Exception as e:
                logger.error(
                    f"<LoggingMiddleware> Error handling streaming response for logging: {e}"
                )
                return "<error-logging-stream>"
        else:
            if hasattr(response, "body"):
                body = response.body  # type: ignore[attr-defined]
                if isinstance(body, bytes):
                    return body.decode("utf-8", errors="ignore")
                elif isinstance(body, str):
                    return body
            return None

    def _sanitize_headers(self, headers: dict) -> dict:
        """Remove or mask sensitive headers."""
        sensitive_keys = {"authorization", "cookie"}
        return {
            k: "****" if k.lower() in sensitive_keys else v for k, v in headers.items()
        }

    def _filter_headers(self, headers: dict) -> dict:
        """Filter headers based on include/exclude rules."""
        return {
            k: v for k, v in headers.items() if k.lower() not in self.exclude_headers
        }

    def _sanitize_body(self, body: Optional[str]) -> Optional[Any]:
        """Sanitize sensitive data in the body."""
        if not body or body in {"<non-utf8-body>"}:
            return body

        try:
            # Attempt to parse as JSON
            data = json.loads(body)
            return self._sanitize_dict(data)
        except json.JSONDecodeError:
            # If not JSON, check for key-value pairs (e.g., form data: "password=abc")
            if "=" in body:
                sanitized = []
                for pair in body.split("&"):
                    key, value = pair.split("=", 1)
                    if key.lower() in SENSITIVE_KEYS:
                        sanitized.append(f"{key}=****")
                    else:
                        sanitized.append(pair)
                return "&".join(sanitized)
            # If plain text, return as-is (or mask if it matches a sensitive key)
            return body if body.lower() not in SENSITIVE_KEYS else "****"

    def _sanitize_dict(self, data: Any) -> Any:
        """Recursively sanitize sensitive keys in a dictionary."""
        if isinstance(data, dict):
            return {
                k: "****" if k.lower() in SENSITIVE_KEYS else self._sanitize_dict(v)
                for k, v in data.items()
            }
        elif isinstance(data, list):
            return [self._sanitize_dict(item) for item in data]
        return data

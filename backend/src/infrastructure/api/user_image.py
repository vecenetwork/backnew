"""Profile picture upload and avatar URL. Supports Supabase Storage via supabase-py or S3-compatible API."""
import logging
import os
import re
import uuid
from typing import cast

import io
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import RedirectResponse
from PIL import Image, ImageOps
from PIL.ImageFile import ImageFile
from pydantic import BaseModel
import pillow_heif  # type: ignore[import-untyped]

from app.exceptions import Missing
from app.schema.user import UserUpdate
from infrastructure.api.dependencies import user_service_dep, token_dependency, current_user_dep, user_repo_dep

logger = logging.getLogger(__name__)

# Register HEIF opener with Pillow
pillow_heif.register_heif_opener()

# Supabase Storage for avatars
SUPABASE_URL = os.getenv("SUPABASE_URL", "").rstrip("/")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
SUPABASE_S3_ACCESS_KEY_ID = os.getenv("SUPABASE_S3_ACCESS_KEY_ID", "")
SUPABASE_S3_SECRET_ACCESS_KEY = os.getenv("SUPABASE_S3_SECRET_ACCESS_KEY", "")
STORAGE_BUCKET = os.getenv("SUPABASE_STORAGE_BUCKET", "profile-pictures")
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000/api")
SIGNED_URL_EXPIRES = 3600  # 1 hour

router = APIRouter()


class ProfilePictureResponse(BaseModel):
    image_url: str


def _use_s3_api() -> bool:
    """Use S3-compatible API when S3 keys are set."""
    return bool(SUPABASE_S3_ACCESS_KEY_ID and SUPABASE_S3_SECRET_ACCESS_KEY)


def _get_s3_endpoint() -> str:
    """Extract S3 endpoint from SUPABASE_URL. e.g. https://xxx.supabase.co -> https://xxx.storage.supabase.co/storage/v1/s3"""
    if not SUPABASE_URL:
        raise ValueError("SUPABASE_URL must be set")
    # Extract project ref: https://abcdef.supabase.co -> abcdef
    match = re.search(r"https?://([a-zA-Z0-9-]+)\.supabase\.co", SUPABASE_URL)
    if not match:
        raise ValueError("SUPABASE_URL must be a valid Supabase project URL (https://xxx.supabase.co)")
    project_ref = match.group(1)
    return f"https://{project_ref}.storage.supabase.co/storage/v1/s3"


def _get_supabase_client():
    """Lazy import to avoid loading supabase when using S3."""
    from supabase import create_client, Client

    if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set")
    return create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)


def _upload_via_supabase(storage_path: str, image_bytes: bytes) -> None:
    """Upload using supabase-py client."""
    supabase = _get_supabase_client()
    supabase.storage.from_(STORAGE_BUCKET).upload(
        storage_path,
        image_bytes,
        {"content-type": "image/jpeg"},
    )


def _upload_via_s3(storage_path: str, image_bytes: bytes) -> None:
    """Upload using boto3 S3-compatible API (Supabase Storage S3)."""
    import boto3
    from botocore.config import Config

    endpoint = _get_s3_endpoint()
    client = boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=SUPABASE_S3_ACCESS_KEY_ID,
        aws_secret_access_key=SUPABASE_S3_SECRET_ACCESS_KEY,
        region_name=os.getenv("SUPABASE_REGION", "us-east-1"),
        config=Config(signature_version="s3v4"),
    )
    client.put_object(
        Bucket=STORAGE_BUCKET,
        Key=storage_path,
        Body=image_bytes,
        ContentType="image/jpeg",
    )


def _create_signed_url_s3(path: str) -> str:
    """Create presigned URL via boto3 for S3-compatible storage."""
    import boto3
    from botocore.config import Config

    endpoint = _get_s3_endpoint()
    client = boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=SUPABASE_S3_ACCESS_KEY_ID,
        aws_secret_access_key=SUPABASE_S3_SECRET_ACCESS_KEY,
        region_name=os.getenv("SUPABASE_REGION", "us-east-1"),
        config=Config(signature_version="s3v4"),
    )
    return client.generate_presigned_url(
        "get_object",
        Params={"Bucket": STORAGE_BUCKET, "Key": path},
        ExpiresIn=SIGNED_URL_EXPIRES,
    )


def _create_signed_url_supabase(path: str) -> str:
    """Create signed URL via supabase-py."""
    supabase = _get_supabase_client()
    result = supabase.storage.from_(STORAGE_BUCKET).create_signed_url(
        path, SIGNED_URL_EXPIRES
    )
    if isinstance(result, list) and result:
        result = result[0]
    if not isinstance(result, dict):
        raise ValueError("Unexpected response from create_signed_url")
    signed_url = result.get("signedURL") or result.get("signed_url") or result.get("path")
    if not signed_url:
        raise ValueError("No signed URL in response")
    return signed_url


def _is_configured() -> bool:
    """Check if storage is configured (either supabase-py or S3)."""
    if _use_s3_api():
        return bool(SUPABASE_URL and SUPABASE_S3_ACCESS_KEY_ID and SUPABASE_S3_SECRET_ACCESS_KEY)
    return bool(SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY)


@router.get("/users/{user_id}/avatar")
async def get_avatar_url(
    user_id: int,
    user_repo: user_repo_dep,
):
    """Redirect to signed URL for user's avatar. Works with private bucket."""
    try:
        user = await user_repo.get_user_by_id(user_id, None)
    except Missing:
        raise HTTPException(status_code=404, detail="User not found")
    if not user or not user.profile_picture:
        raise HTTPException(status_code=404, detail="Avatar not found")
    path = user.profile_picture
    # If it's already a full URL (legacy public bucket), redirect there
    if path.startswith("http"):
        return RedirectResponse(url=path, status_code=302)
    try:
        if _use_s3_api():
            signed_url = _create_signed_url_s3(path)
        else:
            signed_url = _create_signed_url_supabase(path)
        return RedirectResponse(url=signed_url, status_code=302)
    except Exception as e:
        logger.exception("Failed to create signed URL: %s", e)
        raise HTTPException(status_code=500, detail="Failed to load avatar")


@router.post("/upload-profile-picture/", response_model=ProfilePictureResponse)
async def upload_profile_picture(
    token: token_dependency,
    current_user: current_user_dep,
    user_service: user_service_dep,
    file: UploadFile = File(..., description="Image file (JPEG, PNG, HEIC)"),
):
    if not _is_configured():
        if _use_s3_api():
            raise HTTPException(
                status_code=503,
                detail="Avatar upload not configured. Set SUPABASE_URL, SUPABASE_S3_ACCESS_KEY_ID, SUPABASE_S3_SECRET_ACCESS_KEY.",
            )
        raise HTTPException(
            status_code=503,
            detail="Avatar upload not configured. Set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY (or use S3 keys).",
        )

    # Accept standard image types and HEIC/HEIF files
    accepted_types = ["image/", "image/heic", "image/heif"]
    if file.content_type is None or not any(
        file.content_type.startswith(t) or file.content_type == t for t in accepted_types
    ):
        raise HTTPException(
            status_code=400,
            detail="File must be an image (JPEG, PNG, HEIC, HEIF, etc.)",
        )

    try:
        # Read file into memory
        contents = await file.read()
        img_io = io.BytesIO(contents)
        image = cast(ImageFile, Image.open(img_io))
        image = cast(ImageFile, ImageOps.exif_transpose(image))
        image = cast(ImageFile, image.convert("RGB"))

        # Resize image (keeping aspect ratio)
        base_width = 512
        w_percent = base_width / float(image.size[0])
        h_size = int((float(image.size[1]) * float(w_percent)))
        image = cast(
            ImageFile, image.resize((base_width, h_size), Image.Resampling.LANCZOS)
        )

        out_io = io.BytesIO()
        image.save(out_io, format="JPEG", quality=90)
        image_bytes = out_io.getvalue()

        unique_filename = str(uuid.uuid4())
        storage_path = f"{unique_filename}.jpeg"

        if _use_s3_api():
            _upload_via_s3(storage_path, image_bytes)
        else:
            _upload_via_supabase(storage_path, image_bytes)

        # Store path only (private bucket). API returns our avatar endpoint URL.
        await user_service.update_user(
            current_user.id, UserUpdate(profile_picture=storage_path), current_user
        )

        # Return URL that goes through our endpoint (redirects to signed URL)
        image_url = f"{BASE_URL.rstrip('/')}/users/{current_user.id}/avatar"
        return ProfilePictureResponse(image_url=image_url)

    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Avatar upload failed: %s", e)
        raise HTTPException(
            status_code=500,
            detail=f"Avatar upload failed: {str(e)}",
        )

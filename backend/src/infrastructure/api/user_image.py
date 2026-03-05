import logging
import os
import uuid
from typing import cast

import io
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import RedirectResponse
from PIL import Image, ImageOps
from PIL.ImageFile import ImageFile
from pydantic import BaseModel
import pillow_heif  # type: ignore[import-untyped]
from supabase import create_client, Client

from app.exceptions import Missing
from app.schema.user import UserUpdate
from infrastructure.api.dependencies import user_service_dep, token_dependency, current_user_dep, user_repo_dep

logger = logging.getLogger(__name__)

# Register HEIF opener with Pillow
pillow_heif.register_heif_opener()

# Supabase Storage for avatars (private bucket + signed URLs)
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
STORAGE_BUCKET = os.getenv("SUPABASE_STORAGE_BUCKET", "profile-pictures")
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000/api")
SIGNED_URL_EXPIRES = 3600  # 1 hour

router = APIRouter()


class ProfilePictureResponse(BaseModel):
    image_url: str


def _get_supabase() -> Client:
    if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set")
    return create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)


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
        supabase = _get_supabase()
        result = supabase.storage.from_(STORAGE_BUCKET).create_signed_url(
            path, SIGNED_URL_EXPIRES
        )
        # Handle both dict and list (create_signed_urls returns list)
        if isinstance(result, list) and result:
            result = result[0]
        if not isinstance(result, dict):
            raise ValueError("Unexpected response from create_signed_url")
        signed_url = result.get("signedURL") or result.get("signed_url") or result.get("path")
        if not signed_url:
            raise ValueError("No signed URL in response")
        return RedirectResponse(url=signed_url, status_code=302)
    except Exception as e:
        logger.exception("Failed to create signed URL: %s", e)
        raise HTTPException(status_code=500, detail="Failed to load avatar")


@router.post("/upload-profile-picture/", response_model=ProfilePictureResponse)
async def upload_profile_picture(
    token: token_dependency,
    current_user: current_user_dep,
    user_service: user_service_dep,
    file: UploadFile = File(...),
):
    if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
        raise HTTPException(
            status_code=503,
            detail="Avatar upload not configured. Set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY in Railway.",
        )

    # Accept standard image types and HEIC/HEIF files
    accepted_types = ["image/", "image/heic", "image/heif"]
    if file.content_type is None or not any(file.content_type.startswith(t) or file.content_type == t for t in accepted_types):
        raise HTTPException(status_code=400, detail="File must be an image (JPEG, PNG, HEIC, HEIF, etc.)")

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

        supabase = _get_supabase()
        supabase.storage.from_(STORAGE_BUCKET).upload(
            storage_path,
            image_bytes,
            {"content-type": "image/jpeg"},
        )

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

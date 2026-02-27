import uuid
import os
from typing import cast

import boto3  # type: ignore[import-untyped]
import io
from fastapi import APIRouter, File, UploadFile, HTTPException
from PIL import Image, ImageOps
from PIL.ImageFile import ImageFile
from pydantic import BaseModel
import pillow_heif  # type: ignore[import-untyped]

from app.schema.user import UserUpdate
from infrastructure.api.dependencies import user_service_dep, token_dependency, current_user_dep

# Register HEIF opener with Pillow
pillow_heif.register_heif_opener()

# AWS Configuration from environment variables
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "veceai")
AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

# Initialize S3 client - boto3 will automatically load AWS credentials from environment
# Expected environment variables: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION
s3_client = boto3.client("s3", region_name=AWS_REGION)

router = APIRouter()


class ProfilePictureResponse(BaseModel):
    image_url: str


@router.post("/upload-profile-picture/", response_model=ProfilePictureResponse)
async def upload_profile_picture(
    token: token_dependency,
    current_user: current_user_dep,
    user_service: user_service_dep,
    file: UploadFile = File(...),
):
    # Accept standard image types and HEIC/HEIF files
    accepted_types = ["image/", "image/heic", "image/heif"]
    if file.content_type is None or not any(file.content_type.startswith(t) or file.content_type == t for t in accepted_types):
        raise HTTPException(status_code=400, detail="File must be an image (JPEG, PNG, HEIC, HEIF, etc.)")

    # Open image file (supports HEIC/HEIF and standard formats)
    image = cast(ImageFile, Image.open(file.file))
    image = cast(ImageFile, ImageOps.exif_transpose(image))
    image = cast(ImageFile, image.convert("RGB"))

    # Resize image to a larger size (keeping aspect ratio) instead of a small 256px thumbnail
    base_width = 512  # New width for resizing
    w_percent = base_width / float(image.size[0])
    h_size = int((float(image.size[1]) * float(w_percent)))
    image = cast(
        ImageFile, image.resize((base_width, h_size), Image.Resampling.LANCZOS)
    )

    img_io = io.BytesIO()
    image.save(img_io, format="JPEG", quality=90)
    img_io.seek(0)

    unique_filename = str(uuid.uuid4())
    s3_filename = f"profile_pictures/{unique_filename}.jpeg"

    s3_client.upload_fileobj(
        img_io,
        AWS_BUCKET_NAME,
        s3_filename,
        ExtraArgs={
            "ContentType": "image/jpeg",
            # "ACL": "public-read",
        },
    )

    image_url = f"https://{AWS_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{s3_filename}"

    await user_service.update_user(
        current_user.id, UserUpdate(profile_picture=image_url), current_user
    )

    response = ProfilePictureResponse(image_url=image_url)
    return response

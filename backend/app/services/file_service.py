from fastapi import UploadFile, HTTPException
from pathlib import Path
import uuid

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}
MAX_FILE_SIZE_MB = 5


def validate_image(file: UploadFile):
    ext = Path(file.filename).suffix.lower()

    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only JPG and PNG images are allowed."
        )


def generate_safe_filename(original_name: str) -> str:
    ext = Path(original_name).suffix
    return f"{uuid.uuid4()}{ext}"

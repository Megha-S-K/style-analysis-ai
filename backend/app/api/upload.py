from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.file_service import validate_image, generate_safe_filename
from pathlib import Path
import shutil

router = APIRouter()

UPLOAD_DIR = Path("uploads/raw")


@router.post("/upload-image", summary="Upload user image")
async def upload_image(file: UploadFile = File(...)):
    validate_image(file)

    filename = generate_safe_filename(file.filename)
    file_path = UPLOAD_DIR / filename

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to save uploaded image"
        )

    return {
        "message": "Image uploaded successfully",
        "filename": filename
    }

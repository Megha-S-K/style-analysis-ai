from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.services.image_preprocess import preprocess_image

router = APIRouter()

RAW_DIR = Path("uploads/raw")
PROCESSED_DIR = Path("uploads/processed")


@router.post("/preprocess-image", summary="Preprocess uploaded image")
def preprocess_uploaded_image(filename: str):
    input_path = RAW_DIR / filename
    output_path = PROCESSED_DIR / filename

    if not input_path.exists():
        raise HTTPException(status_code=404, detail="Image not found")

    try:
        processed_path = preprocess_image(input_path, output_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "message": "Image preprocessed successfully",
        "processed_path": processed_path
    }

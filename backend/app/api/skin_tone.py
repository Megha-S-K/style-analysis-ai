from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.services.face_detection import extract_face
from app.services.skin_tone import detect_skin_undertone

router = APIRouter()

PROCESSED_DIR = Path("uploads/processed")


@router.post("/skin-undertone", summary="Detect skin undertone")
def get_skin_undertone(filename: str):
    image_path = PROCESSED_DIR / filename

    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Processed image not found")

    try:
        face = extract_face(image_path)
        result = detect_skin_undertone(face)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "filename": filename,
        "skin_analysis": result
    }

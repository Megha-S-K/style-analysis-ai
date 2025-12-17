from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.services.pose_estimation import extract_pose_landmarks

router = APIRouter()

PROCESSED_DIR = Path("uploads/processed")


@router.post("/pose-landmarks", summary="Extract body pose landmarks")
def get_pose_landmarks(filename: str):
    image_path = PROCESSED_DIR / filename

    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Processed image not found")

    try:
        landmarks = extract_pose_landmarks(image_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "filename": filename,
        "num_landmarks": len(landmarks),
        "landmarks": landmarks
    }

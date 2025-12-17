from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.services.pose_estimation import extract_pose_landmarks
from app.services.body_measurements import estimate_body_measurements

router = APIRouter()

PROCESSED_DIR = Path("uploads/processed")


@router.post("/body-measurements", summary="Estimate body measurements")
def get_body_measurements(filename: str):
    image_path = PROCESSED_DIR / filename

    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Processed image not found")

    try:
        landmarks = extract_pose_landmarks(image_path)
        measurements = estimate_body_measurements(landmarks)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "filename": filename,
        "measurements": measurements
    }

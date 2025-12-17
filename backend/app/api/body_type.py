from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.services.pose_estimation import extract_pose_landmarks
from app.services.body_measurements import estimate_body_measurements
from app.services.body_type_classifier import classify_body_type

router = APIRouter()

PROCESSED_DIR = Path("uploads/processed")


@router.post("/body-type", summary="Classify body type")
def get_body_type(filename: str):
    image_path = PROCESSED_DIR / filename

    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Processed image not found")

    try:
        landmarks = extract_pose_landmarks(image_path)
        measurements = estimate_body_measurements(landmarks)
        classification = classify_body_type(measurements)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "filename": filename,
        "body_type_analysis": classification
    }

from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.services.pose_estimation import extract_pose_landmarks
from app.services.body_measurements import estimate_body_measurements
from app.services.body_type_classifier import classify_body_type
from app.services.face_detection import extract_face
from app.services.skin_tone import detect_skin_undertone
from app.services.style_engine import recommend_style

router = APIRouter()

PROCESSED_DIR = Path("uploads/processed")


@router.post("/style-recommendation", summary="Generate style and color recommendations")
def get_style_recommendation(filename: str):
    image_path = PROCESSED_DIR / filename

    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Processed image not found")

    try:
        # Body analysis
        landmarks = extract_pose_landmarks(image_path)
        measurements = estimate_body_measurements(landmarks)
        body_type_result = classify_body_type(measurements)

        # Skin analysis
        face = extract_face(image_path)
        skin_result = detect_skin_undertone(face)

        # Style recommendation
        recommendations = recommend_style(
            body_type=body_type_result["body_type"],
            undertone=skin_result["undertone"]
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "filename": filename,
        "body_type": body_type_result,
        "skin_undertone": skin_result,
        "style_recommendation": recommendations
    }

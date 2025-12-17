
from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.services.pose_estimation import extract_pose_landmarks
from app.services.body_measurements import estimate_body_measurements
from app.services.body_type_classifier import classify_body_type
from app.services.face_detection import extract_face
from app.services.skin_tone import detect_skin_undertone
from app.services.style_engine import recommend_style
from app.services.explanation_generator import generate_style_explanation

router = APIRouter()

PROCESSED_DIR = Path("uploads/processed")


@router.post("/style-explanation", summary="Generate human-friendly style explanation")
def get_style_explanation(filename: str):
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

        # Style logic
        style_recommendation = recommend_style(
            body_type=body_type_result["body_type"],
            undertone=skin_result["undertone"]
        )

        # GenAI-style explanation
        explanation = generate_style_explanation(
            body_type_result,
            skin_result,
            style_recommendation
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "filename": filename,
        "explanation": explanation
    }

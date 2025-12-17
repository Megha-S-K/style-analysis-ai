def classify_body_type(measurements: dict):
    """
    Classifies body type based on shoulder-to-hip and waist-to-hip ratios.
    Returns body type with confidence score.
    """

    ratios = measurements["ratios"]
    shoulder_hip = ratios["shoulder_to_hip"]
    waist_hip = ratios["waist_to_hip"]

    # Default values
    body_type = "Unknown"
    confidence = 0.0

    # Rule-based classification
    if shoulder_hip > 1.05 and waist_hip < 0.95:
        body_type = "Athletic"
        confidence = 0.85

    elif waist_hip < 0.85:
        body_type = "Slim"
        confidence = 0.80

    elif waist_hip >= 0.95 and shoulder_hip <= 1.0:
        body_type = "Curvy"
        confidence = 0.82

    else:
        body_type = "Broad"
        confidence = 0.75

    return {
        "body_type": body_type,
        "confidence": confidence,
        "explanation": (
            f"Classification based on shoulder-to-hip ratio ({round(shoulder_hip,2)}) "
            f"and waist-to-hip ratio ({round(waist_hip,2)})."
        )
    }

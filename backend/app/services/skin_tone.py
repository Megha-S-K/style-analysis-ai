import cv2
import numpy as np


def detect_skin_undertone(face_image):
    """
    Detects skin undertone using LAB color space.
    Returns Warm / Cool / Neutral with confidence.
    """

    # Convert to LAB color space
    lab = cv2.cvtColor(face_image, cv2.COLOR_BGR2LAB)

    # Extract A and B channels
    a_channel = lab[:, :, 1]
    b_channel = lab[:, :, 2]

    avg_a = np.mean(a_channel)
    avg_b = np.mean(b_channel)

    # Rule-based undertone classification
    if avg_b - avg_a > 10:
        undertone = "Warm"
        confidence = 0.85
    elif avg_a - avg_b > 10:
        undertone = "Cool"
        confidence = 0.85
    else:
        undertone = "Neutral"
        confidence = 0.75

    return {
        "undertone": undertone,
        "confidence": confidence,
        "explanation": (
            f"Classification based on LAB color space analysis "
            f"(avg A={round(avg_a,2)}, avg B={round(avg_b,2)})."
        )
    }

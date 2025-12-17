import math


def euclidean_distance(p1, p2):
    return math.sqrt(
        (p1["x"] - p2["x"]) ** 2 +
        (p1["y"] - p2["y"]) ** 2
    )


def estimate_body_measurements(landmarks: list):
    """
    Estimates relative body measurements using pose landmarks.
    Returns normalized ratios (scale-invariant).
    """

    left_shoulder = landmarks[11]
    right_shoulder = landmarks[12]
    left_hip = landmarks[23]
    right_hip = landmarks[24]

    shoulder_width = euclidean_distance(left_shoulder, right_shoulder)
    hip_width = euclidean_distance(left_hip, right_hip)

    # Approx waist estimation as midpoint between shoulders and hips
    waist_width = (shoulder_width + hip_width) / 2

    # Normalize ratios
    shoulder_to_hip_ratio = shoulder_width / hip_width if hip_width else 0
    waist_to_hip_ratio = waist_width / hip_width if hip_width else 0

    return {
        "shoulder_width": round(shoulder_width, 4),
        "waist_width": round(waist_width, 4),
        "hip_width": round(hip_width, 4),
        "ratios": {
            "shoulder_to_hip": round(shoulder_to_hip_ratio, 4),
            "waist_to_hip": round(waist_to_hip_ratio, 4)
        }
    }

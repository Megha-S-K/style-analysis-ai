import cv2
import mediapipe as mp
from pathlib import Path

mp_pose = mp.solutions.pose


def extract_pose_landmarks(image_path: Path):
    """
    Runs MediaPipe Pose on an image and returns landmark coordinates.
    """
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError("Unable to read image")

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_pose.Pose(static_image_mode=True) as pose:
        result = pose.process(image_rgb)

        if not result.pose_landmarks:
            raise ValueError("No human pose detected")

        landmarks = []
        for lm in result.pose_landmarks.landmark:
            landmarks.append({
                "x": lm.x,
                "y": lm.y,
                "z": lm.z,
                "visibility": lm.visibility
            })

    return landmarks

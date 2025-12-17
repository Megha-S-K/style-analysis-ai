from pathlib import Path
from PIL import Image, ImageOps
import numpy as np

TARGET_SIZE = (512, 512)


def preprocess_image(input_path: Path, output_path: Path):
    """
    Loads an image, fixes orientation, resizes, normalizes,
    and saves a processed version.
    """
    try:
        image = Image.open(input_path)
    except Exception:
        raise ValueError("Invalid image file")

    # Fix orientation using EXIF data
    image = ImageOps.exif_transpose(image)

    # Convert to RGB
    image = image.convert("RGB")

    # Resize
    image = image.resize(TARGET_SIZE)

    # Normalize (0–255 → 0–1)
    image_array = np.array(image) / 255.0

    # Convert back to image for saving
    processed_image = Image.fromarray((image_array * 255).astype("uint8"))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    processed_image.save(output_path)

    return str(output_path)

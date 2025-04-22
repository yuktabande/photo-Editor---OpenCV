import cv2
import os
import numpy as np

def load_image(image_path: str) -> np.ndarray:
    """
    Loads an image from the specified file path.

    Args:
        image_path (str): Path to the image file.

    Returns:
        np.ndarray: Loaded image as a NumPy array.

    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the image cannot be loaded (e.g., invalid format).
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to load image. Ensure {image_path} is a valid image file.")
    print(f"Image successfully loaded from {image_path}")
    return image

def save_image(image: np.ndarray, output_path: str):
    """
    Saves the image to the specified file path.

    Args:
        image (np.ndarray): Image to save.
        output_path (str): Path to save the image.

    Raises:
        IOError: If the image cannot be saved.
    """
    success = cv2.imwrite(output_path, image)
    if not success:
        raise IOError(f"Failed to save image to {output_path}")
    print(f"Image successfully saved to {output_path}")
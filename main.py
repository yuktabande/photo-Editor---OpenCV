import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from filters import apply_grayscale, apply_sepia, apply_negative, apply_blur, apply_edge_detection
from transform import rotate_image, resize_image, adjust_brightness_contrast
from utils import load_image, save_image

def main():
    img_path = "test_images/img.jpg"
    output_path = "test_images/edited.jpg"

    # Load image
    img = load_image(img_path)

    # Apply transformations
    img = apply_sepia(img)
    img = rotate_image(img, 45)
    img = resize_image(img, 400, 400)
    img = adjust_brightness_contrast(img, brightness=30, contrast=1.2)

    # Save output
    save_image(img, output_path)
    print(f"Edited image saved to {output_path}")

if __name__ == "__main__":
    main()
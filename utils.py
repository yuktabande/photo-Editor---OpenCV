import cv2
import os

def load_image(path):
    if not os.path.exists(path):
        raise FileNotFoundError("Image not found at path: " + path)
    return cv2.imread(path)

def save_image(img, path):
    cv2.imwrite(path, img)
import cv2
import numpy as np

def apply_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def apply_sepia(img):
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    sepia = cv2.transform(img, kernel)
    return np.clip(sepia, 0, 255).astype(np.uint8)

def apply_negative(img):
    return cv2.bitwise_not(img)

def apply_blur(img, ksize=15):
    # Ensure ksize is an odd number and greater than 1
    if ksize % 2 == 0:
        ksize += 1  # Make it odd if it's even
    if ksize < 1:
        ksize = 3  # Default to 3 if it's less than 1
    
    return cv2.GaussianBlur(img, (ksize, ksize), 0)

def apply_edge_detection(img):
    return cv2.Canny(img, 100, 200)
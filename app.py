import streamlit as st
import numpy as np
from PIL import Image
import io
import cv2

# Import functions from your backend files
from filters import apply_grayscale, apply_sepia, apply_negative, apply_blur, apply_edge_detection
from transform import rotate_image, resize_image, adjust_brightness_contrast
from utils import load_image, save_image

# Function to process the uploaded image and convert it to numpy array (OpenCV format)
def process_image(uploaded_image):
    img = Image.open(uploaded_image)
    img = np.array(img)

    # Convert RGB to BGR (OpenCV uses BGR by default)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img

# Streamlit UI
st.title("Interactive Image Editing with Filters")

# File upload (Dropbox)
uploaded_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Process the uploaded image
    img = process_image(uploaded_file)

    # Display the uploaded image
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Filter buttons and intensity sliders
    filter = st.radio("Choose a filter:", ["None", "Grayscale", "Sepia", "Negative", "Blur", "Edge Detection", "Rotate", "Resize", "Brightness/Contrast"])

    if filter == "Grayscale":
        img = apply_grayscale(img)
        st.image(img, caption="Grayscale Image", use_container_width=True)

    elif filter == "Sepia":
        img = apply_sepia(img)
        st.image(img, caption="Sepia Image", use_container_width=True)

    elif filter == "Negative":
        img = apply_negative(img)
        st.image(img, caption="Negative Image", use_container_width=True)

    elif filter == "Blur":
        blur_intensity = st.slider("Blur Intensity", 1, 20, 5)
        img = apply_blur(img, blur_intensity)
        st.image(img, caption="Blurred Image", use_container_width=True)

    elif filter == "Edge Detection":
        img = apply_edge_detection(img)
        st.image(img, caption="Edge Detection", use_container_width=True)

    elif filter == "Rotate":
        rotation_angle = st.slider("Rotation Angle", 0, 360, 45)
        img = rotate_image(img, rotation_angle)
        st.image(img, caption="Rotated Image", use_container_width=True)

    elif filter == "Resize":
        width = st.slider("Width", 50, 1000, 400)
        height = st.slider("Height", 50, 1000, 400)
        img = resize_image(img, width, height)
        st.image(img, caption="Resized Image", use_container_width=True)

    elif filter == "Brightness/Contrast":
        brightness = st.slider("Brightness", -100, 100, 0)
        contrast = st.slider("Contrast", 0.1, 3.0, 1.0)
        img = adjust_brightness_contrast(img, brightness, contrast)
        st.image(img, caption="Brightness/Contrast Adjusted", use_container_width=True)

    # Allow user to download the final image
    img_pil = Image.fromarray(img)
    buffered = io.BytesIO()
    img_pil.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()

    st.download_button(label="Download Image", data=img_bytes, file_name="edited_image.png", mime="image/png")
import os
import urllib.request
import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image

MODEL_PATH = "model.keras"
URL = "https://github.com/HackWithSaksham/Face-Mask-Detection/releases/download/v1.0/model.keras"

if not os.path.exists(MODEL_PATH):
    print("Downloading model...")
    urllib.request.urlretrieve(URL, MODEL_PATH)

# Load model
model = load_model(MODEL_PATH,compile=False)

# Load face detector
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

st.title("Face Mask Detection 😷")

# -------- Prediction --------
def detect_face_mask(img):
    # Ensure correct size
    img = cv2.resize(img, (224, 224))

    # Ensure 3 channels (VERY IMPORTANT FIX)
    if img.shape[-1] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    img = img.astype("float32") / 255.0
    img = np.reshape(img, (1, 224, 224, 3))

    return model.predict(img, verbose=0)[0][0]


# -------- Face Detection --------
def detect_face(gray):
    return face_cascade.detectMultiScale(gray, 1.3, 5)


# -------- Label --------
def draw_label(img, text, pos, bg_color):
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 1)

    end_x = pos[0] + text_size[0][0] + 10
    end_y = pos[1] - text_size[0][1] - 10

    cv2.rectangle(img, pos, (end_x, pos[1] - 30), bg_color, -1)
    cv2.putText(img, text, (pos[0], pos[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)


# -------- Process Image --------
def process_image(frame):
    # Convert PIL -> RGB -> numpy
    frame = frame.convert("RGB")   # 🔥 CRITICAL FIX
    img = np.array(frame)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    coords = detect_face(gray)

    for (x, y, w, h) in coords:
        face = img[y:y+h, x:x+w]

        y_pred = detect_face_mask(face)

        if y_pred > 0.5:
            draw_label(img, "Mask", (x, y), (0, 255, 0))
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        else:
            draw_label(img, "No Mask", (x, y), (0, 0, 255))
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    return img


# -------- UI OPTION --------
option = st.radio("Choose Input Method:", ["Upload Image", "Use Webcam"])

# -------- Upload --------
if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")  # 🔥 FIX
        st.image(image, caption="Uploaded Image")

        result = process_image(image)
        st.image(result, caption="Result")


# -------- Webcam --------
elif option == "Use Webcam":
    camera_image = st.camera_input("Take a picture")

    if camera_image is not None:
        image = Image.open(camera_image).convert("RGB")  # 🔥 FIX
        st.image(image, caption="Captured Image")

        result = process_image(image)
        st.image(result, caption="Result")
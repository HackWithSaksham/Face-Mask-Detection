import os
import gdown   # pip install gdown
import streamlit as st
import numpy as np
import cv2
from keras.models import load_model
from PIL import Image

MODEL_PATH = "model.h5"

if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/uc?id=1tPOCyMnlbAJIh-8ikOeBald_1-55kw2W"
    gdown.download(url, MODEL_PATH, quiet=False)

# Load model
model = load_model("model.h5")

# Load face detector
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

st.title("Face Mask Detection 😷")

# -------- Prediction --------
def detect_face_mask(img):
    img = cv2.resize(img, (224, 224))
    img = img.astype("float32") / 255.0
    img = img.reshape(1, 224, 224, 3)
    return model.predict(img)[0][0]

# -------- Face Detection --------
def detect_face(img):
    return face_cascade.detectMultiScale(img)

# -------- Label --------
def draw_label(img,text,pos,bg_color):
    text_size=cv2.getTextSize(text,cv2.FONT_HERSHEY_SIMPLEX,1,cv2.FILLED)

    end_x=pos[0]+text_size[0][0]+2
    end_y=pos[1]+text_size[0][1]-2

    cv2.rectangle(img,pos,(end_x,end_y),bg_color,cv2.FILLED)
    cv2.putText(img,text,pos,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1,cv2.LINE_AA)

# -------- Process Image --------
def process_image(frame):
    img = np.array(frame)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    coords = detect_face(gray)

    for (x, y, w, h) in coords:
        face = img[y:y+h, x:x+w]

        face = cv2.resize(face, (224,224))
        y_pred = detect_face_mask(face)

        if y_pred > 0.5:
            draw_label(img, "Mask", (x, y), (0,255,0))
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        else:
            draw_label(img, "No Mask", (x, y), (0,0,255))
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    return img

# -------- UI OPTION --------
option = st.radio("Choose Input Method:", ["Upload Image", "Use Webcam"])

# -------- Upload --------
if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")

        result = process_image(image)
        st.image(result, caption="Result")

# -------- Webcam --------
elif option == "Use Webcam":
    camera_image = st.camera_input("Take a picture")

    if camera_image is not None:
        image = Image.open(camera_image)
        st.image(image, caption="Captured Image")

        result = process_image(image)
        st.image(result, caption="Result")
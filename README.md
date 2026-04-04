# 😷 Face Mask Detection System

A deep learning-based web application that detects whether a person is wearing a face mask or not using image upload or webcam input.

---

## 🚀 Features

- 📷 Upload image for prediction  
- 📸 Capture image using webcam (browser)  
- 😀 Face detection using Haar Cascade  
- 🧠 Mask classification using deep learning  
- ⚡ Real-time prediction  
- 🌐 Interactive UI built with Streamlit  

---

## 🧠 Model Overview

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/1*2J9Y8ZP5QkKZp0a0pXh8Mg.png" width="500"/>
</p>

- Architecture: **VGG16 (Transfer Learning)**
- Framework: **TensorFlow / Keras**
- Input Size: **224 × 224**
- Output:
  - ✅ Mask
  - ❌ No Mask

---

## 📸 Sample Predictions

<p align="center">
  <img src="https://raw.githubusercontent.com/chandrikadeb7/Face-Mask-Detection/master/dataset/with_mask/0-with-mask.jpg" width="200"/>
  <img src="https://raw.githubusercontent.com/chandrikadeb7/Face-Mask-Detection/master/dataset/without_mask/0.jpg" width="200"/>
</p>

- 🟢 Left: Mask Detected  
- 🔴 Right: No Mask Detected  

---

## 🛠️ Tech Stack

- Python  
- TensorFlow / Keras  
- OpenCV  
- Streamlit  
- NumPy  
- Pillow  

---

## 📂 Project Structure
Face-Mask-Detection/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── haarcascade_frontalface_default.xml
├── README.md
├── Procfile
├── Face_Mask_Detection.ipynb
├── train
├── test
├── outputs


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Face-Mask-Detection.git
cd Face-Mask-Detection
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### pip install -r requirements.txt
``` bash
3️⃣ Run the application
```

---

## 📦 Model File

### ⚠️ The model file is not included in this repository due to size limitations.

### 👉 The application automatically downloads the model at runtime using Google Drive.

---

## 🌐 Deployment

### This project is deployed using Render with Streamlit.

---

## 🚀 Future Improvements

### 🐳 Docker-based deployment
### ☁️ Deploy on Hugging Face S

---

## 🤝 Contributing

### Contributions are welcome! Feel free to fork the repo and improve it.

---

## 📜 License

### This project is open-source and available under the MIT License.

---

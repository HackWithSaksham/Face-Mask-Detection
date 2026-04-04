<!-- FACE MASK README -->

<div align="center">

# 😷 **Face Mask Detection**
### *Real-time Face Mask Prediction using Deep Learning*

> A **Computer Vision model** that detects whether a person is wearing a **face mask or not** using a trained **Convolutional Neural Network (CNN)**.  
> The system can analyze images or video frames and classify faces as **Mask** or **No Mask**.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-green?style=for-the-badge)
![Model](https://img.shields.io/badge/Model-CNN-red?style=for-the-badge)

</div>

---

# 🪄 About the Project

**Face Mask Detection** is a deep learning project that predicts whether a person in an image is **wearing a mask or not**.

The model is trained using **image datasets of masked and unmasked faces** and uses **computer vision techniques** to classify faces.

This project demonstrates how **AI can be used for public health monitoring**, especially in situations like **pandemic safety systems, surveillance, and automated compliance monitoring**.

---

# ⚡ Key Features

| ✨ Feature | 💬 Description |
|------------|---------------|
| 😷 **Mask Detection** | Detects whether a face is wearing a mask or not |
| 🧠 **Deep Learning Model** | CNN-based model trained on face images |
| 📷 **Image Processing** | Uses OpenCV for image preprocessing |
| ⚡ **Real-Time Prediction** | Can be integrated with webcam/video streams |
| 🧮 **High Accuracy Model** | Trained with optimized CNN architecture |
| 💾 **Model Serialization** | Saved using `pickle` for deployment |
| 🧩 **Easy Deployment** | Can be integrated into Streamlit or web apps |

---

# 🧰 Technologies Used

<div align="center">

| Layer | Technologies |
|------|--------------|
| 🐍 **Programming Language** | Python |
| 📊 **Data Processing** | NumPy · Pandas |
| 🧠 **Deep Learning** | TensorFlow · Keras |
| 👁 **Computer Vision** | OpenCV |
| 📈 **Model Training** | CNN Architecture |
| 💾 **Model Storage** | Pickle |
| 📓 **Development Environment** | Jupyter Notebook |

</div>

---

# 🧠 Model Workflow

The Face Mask Detection system follows the workflow below:

1️⃣ **Dataset Collection**  
Images of faces with and without masks are collected.

2️⃣ **Image Preprocessing**
- Resize images
- Normalize pixel values
- Convert images to arrays

3️⃣ **Model Training**

A **Convolutional Neural Network (CNN)** is trained to classify images into:

- **Mask**
- **No Mask**

4️⃣ **Model Evaluation**

The trained model is evaluated using validation data to measure performance.

5️⃣ **Prediction**

The trained model predicts whether a person is **wearing a mask or not**.

---

# 📁 Project Structure

```bash
Face-Mask-Detection/
│
├── dataset/                # Training images
│   ├── with_mask/
│   └── without_mask/
│
├── model/
│   └── model.pkl           # Trained ML model
│
├── face_mask_model.ipynb   # Model training notebook
│
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

# 📊 Model Architecture

The model uses a **Convolutional Neural Network (CNN)** consisting of:

- Convolution Layers
- MaxPooling Layers
- Flatten Layer
- Dense Layers
- Output Layer (Binary Classification)

The output predicts:

```
0 → No Mask
1 → Mask
```

---

# 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/face-mask-detection.git
cd face-mask-detection
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the notebook

Open the notebook:

```
face_mask_model.ipynb
```

Run all cells to:

- preprocess the dataset
- train the CNN model
- evaluate performance
- save the trained model

---

# 💾 Model Output

The trained model is saved as:

```
model.pkl
```

This model can be used in:

- Web applications
- Surveillance systems
- Real-time mask detection apps

---

# 📌 Future Improvements

Possible improvements for the project:

- 🎥 **Real-time webcam detection**
- 🌐 **Deploy using Streamlit**
- 📱 **Mobile app integration**
- 🧠 **Use transfer learning (MobileNet, ResNet)**
- ☁ **Deploy on cloud platforms**

---

# 👨‍💻 Author

**Saksham Garg**  
💻 Machine Learning & AI Enthusiast

<div align="center">

⭐ If you like this project, consider giving it a **star**!

Made with ❤️ by **Saksham Garg**

</div>

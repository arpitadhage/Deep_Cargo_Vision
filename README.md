# 🚀 Deep CargoVision

AI-powered cargo inspection system for automated X-ray analysis, threat detection, and manifest validation using deep learning.

---

## 🎥 Demo Video

👉 [Watch Demo](https://drive.google.com/file/d/12S3OFV0OLL094COQ0BBeVxMqNZV9FaxB/view?usp=drive_link)

## 🧠 Overview

**Deep CargoVision** is an intelligent cargo inspection platform designed for customs and security operations. It automates the analysis of X-ray cargo images using multiple deep learning models to detect threats, validate manifests, and generate risk insights.

---

## 🔥 Key Features

* 📦 Single & batch X-ray image analysis
* 🔍 YOLO-based object detection with bounding boxes
* ⚠️ AI-driven risk scoring & anomaly detection
* 📋 Cargo manifest validation (CSV-based)
* 🦎 Wildlife smuggling detection (Reptiles, Birds, Mammals)
* 💧 Liquid container detection (Bottles, Cans, Sprays)
* 📊 Batch analytics & trend visualization
* 🎯 Multi-model inference (YOLO + EfficientNet)
* 🔒 Security-focused dashboard (dark mode UI)

---

## 🏗️ System Architecture

* **Detection Layer** → YOLOv8 (object localization)
* **Classification Layer** → EfficientNet / ResNet18 (refinement)
* **Risk Engine** → Weighted scoring system
* **Validation Layer** → Manifest cross-checking

---

## ⚙️ Tech Stack

### Frontend

* React 19 + Vite
* Tailwind CSS
* Framer Motion
* Recharts

### Backend

* FastAPI
* Python 3.10+

### Machine Learning

* YOLOv8 (Detection)
* EfficientNet / ResNet18 (Classification)
* PyTorch

---

## 📂 Project Structure

```
ai-cargo-detection/
├── src/                # Frontend (React)
├── backend/            # FastAPI backend
├── model/              # Trained models
├── training-notebooks/ # Model training
├── public/             # Static files
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone Repository

```
git clone https://github.com/arpitadhage/Deep_Cargo_Vision.git
cd Deep_Cargo_Vision
```

### 2. Frontend Setup

```
npm install
npm run dev
```

### 3. Backend Setup

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

---

## 🧪 Models Used

| Model          | Purpose              |
| -------------- | -------------------- |
| YOLOv8         | Object detection     |
| EfficientNet   | Image classification |
| Wildlife Model | Fauna detection      |
| Liquid Model   | Container detection  |

---

## 📊 Core Capabilities

### 🔹 Standard Scan (YOLO)

* Fast object detection
* Real-time bounding boxes
* Threat scoring

### 🔹 Deep Forensic Scan

* Two-stage pipeline (YOLO → Classification)
* Higher accuracy
* Reduced false positives

### 🔹 Wildlife Detection

* Detects illegal fauna transport

### 🔹 Liquid Detection

* Identifies hazardous/restricted liquids

---

## 📡 API Endpoints (Sample)

* `POST /predict` → YOLO detection
* `POST /predict-efficientnet` → Deep scan
* `POST /predict-wildlife` → Wildlife detection
* `POST /predict-liquid` → Liquid detection
* `GET /health` → System status

---

## 📈 Performance Highlights

* Classification Accuracy: ~92%
* Pipeline Accuracy: ~86.4%
* YOLO mAP@50: ~78.5%
* Wildlife Detection mAP: ~96%

---

## 🔐 Security Notes

* No data stored between sessions
* Local processing supported
* Designed for authorized personnel

---

## 📌 Future Improvements

* Real-time video stream analysis
* Cloud deployment (AWS/GCP)
* Model optimization for edge devices
* Advanced anomaly detection

---

## 🤝 Contributing

Contributions are welcome!

* Follow project structure
* Test model changes
* Update documentation

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!

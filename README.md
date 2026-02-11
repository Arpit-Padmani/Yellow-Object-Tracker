# 🟡 Yellow Object Detector (Live)

A lightweight, real-time computer vision application that identifies and tracks yellow objects using a live webcam feed. This project uses **OpenCV** and **Python** to process video frames and isolate specific color ranges.

---

## ✨ Features

* **Real-time Detection:** Processes live video stream with minimal latency.
* **Color Masking:** Uses HSV color space for accurate yellow detection.
* **Visual Feedback:** Draws bounding boxes (or contours) around detected objects in the live preview.
* **Easy Setup:** Simple environment configuration and execution.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Library:** OpenCV (cv2)
* **Environment:** PyCharm / VS Code

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python installed. You will also need to install the OpenCV library:

```bash
pip install opencv-python

```

### 2. Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/your-repo-name.git
cd your-repo-name

```

### 3. Running the Project

Connect your webcam and run the main script:

```bash
python main.py

```

*Press **'q'** to exit the camera window.*

## 🧠 How It Works

1. **Frame Capture:** The app captures frames from the webcam.
2. **Color Conversion:** Converts BGR frames to **HSV** (Hue, Saturation, Value) for better color segmentation.
3. **Thresholding:** Applies a mask to filter out everything except the "Yellow" range.
4. **Contour Mapping:** Finds the edges of the yellow shapes and draws a tracking box around them.

## 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

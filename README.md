# 🧠 AI Module:OpenCV for Image Processing

This project showcases a series of hands-on tasks to build foundational skills in **Python programming**, **OpenCV**, and **computer vision**. The work includes game logic, video transformations, template matching, and image enhancement using filters. It was created as a recruitment task for a technical club and serves as a portfolio project demonstrating applied computer vision techniques.

---

## 🧩 Project Structure

### 🔹 1. Rock-Paper-Scissor Game 🎮

**Objective**: Use Python to create a CLI-based interactive game simulating rock-paper-scissors.  
**Key Concepts**: Randomness, control flow, user input handling.

**Features**:
- Player vs Computer gameplay  
- Score tracking  
- Multiple rounds  

📁 **Folder**: `rock-paper-scissors-game`  
🧾 **Submission**: Python code + game results

---

### 🔹 2. Image Processing & OpenCV 🎥

#### 📌 2A. Video Manipulation (Virat Kohli Clip)

**Objective**: Manipulate video data to apply transformations and filters using OpenCV.

**Tasks Completed**:
- Mirrored the video in four directions: horizontal, vertical, diagonal, and 180°
- Applied:
  - HSV color detection (Green color filter)
  - Custom artistic effects:
    - Grayscale
    - Inverted colors
    - Sketch effect

📁 **Folder**: `video-manipulation`  
🎞️ **Submission**: Transformed videos (.mp4) + Python code

---

#### 📌 2B. Template Matching (Digit Dataset)

**Objective**: Detect digits from template images using OpenCV template matching.

**Tasks Completed**:
- Preprocessed and loaded digit templates (0–9)
- Used `cv2.matchTemplate()` to find matches in full images
- Drew bounding boxes around detected digits
- Generated 20 final output images with detections

📁 **Folder**: `template-matching`  
🧾 **Submission**: Code + 20 processed output images

---

#### 📌 2C. Underwater Image Enhancement

**Objective**: Apply and evaluate different OpenCV filters to enhance underwater images.

**Steps Followed**:
- Selected 4 underwater images
- Applied 5 distinct OpenCV filters:
  - CLAHE (Contrast Limited Adaptive Histogram Equalization)
  - Bilateral Filtering
  - White Balance Correction
  - Histogram Equalization
  - Sharpening
- Documented the purpose and effect of each filter

📁 **Folder**: `underwater-image-enhancement`  
📝 **Submission**: 
- Images named like `1_filtername.jpg`
- Purpose and explanation of each filter
- Code for the filters

---

## 🔧 Tech Stack

**Language**: Python 3.8+  

**Libraries Used**:
- `OpenCV` for image/video processing
- `NumPy`, `Matplotlib` for visualization
- `random`, `os`, `glob` for data handling

---

## 🏁 How to Run

### 🔹 Clone this repository

```bash
git clone https://github.com/your-username/aimodule-opencv-tasks.git
cd aimodule-opencv-tasks


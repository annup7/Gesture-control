# 🎮 Gesture Controlled Subway Surfers & Temple Run

Control the classic **Subway Surfers** & **Temple Run** game using just your **hand gestures** via webcam — no keyboard or controller required! This project combines **Computer Vision**, **MediaPipe**, and **PyAutoGUI** to enable an immersive hands-free gaming experience.

---

## ✨ Features

- 🖐️ Real-time hand gesture recognition using **MediaPipe**
- 🎮 Map gestures to Subway Surfers/Temple Run controls (left, right, jump, slide)
- ⚙️ Easy-to-use and beginner-friendly Python code
- 💻 Works with any laptop or USB webcam
- 🔄 No modification needed to the game itself

---

## 🛠️ Tech Stack

- **Python 3.x**
- **OpenCV** – Image processing and webcam input
- **MediaPipe** – Hand tracking and gesture detection
- **PyAutoGUI** – Automating keyboard actions
- **NumPy**, **Time**, **Math**, and other standard Python modules

---

## 🧠 Gesture Mapping

| Gesture                       | Action in Game       |
|-------------------------------|----------------------|
| ✋ Open Palm (5 fingers)     | Slide                |
| ☝️ Index finger **up** only  | Jump                 |
| 👉 Pointing Right (Thumb)    | Move Right           |
| 👈 Pointing Left (Thumb)     | Move Left            |
| ✊ Fist                      | No Action / Neutral  |

> 💡 Gestures can be customized in the code by editing `main.py`.

---

## 🚀 Getting Started

### 1. Clone this repository
```bash
git clone https://github.com/annup7/Gesture-control.git
cd Gesture-control
```

### 2. (Optional) Create & activate a virtual environment
```bash
python -m venv env
.\env\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the gesture control
```bash
python main.py
```

> ⚠️ Make sure **Subway Surfers or Temple Run is running on [Poki](https://poki.com/en/g/subway-surfers) or is open and running in the background** before launching the script.

---

## 📜 License

This project is open-source and available under the **MIT License**.  
Feel free to use, modify, and share it for your own fun or learning.

# 🎥 Bubbles_The_Dev-Screen-Recorder 🖥️

Welcome to the **Screen Recorder App**! This is a simple tool to record your screen with mouse highlighting to enhance visibility, perfect for creating tutorials or demos. 🖱️✨

## Features 🚀

- **Simple and Easy to Use** 🛠️
- **Records Screen at 60 FPS** 🖥️💨
- **Highlights Mouse Cursor** for Better Visibility 🖱️👀
- **Saves Recording as an MP4 Video** 🎬

### [Bubbles_The_Dev-Screen-Recorder-App.EXE](https://github.com/KernFerm/screen-recorder-app/releases/tag/recorder)

## 🚀 Demo

![Sample Video](https://github.com/KernFerm/screen-recorder-app/blob/main/Sample_Video/screen_recording.gif)

## Installation 🔧

To get started with this project, you'll need the following Python libraries:

1. **OpenCV** `cv2`
2. **Pillow** `PIL`
3. **PyAutoGUI** `pyautogui`
4. **NumPy** `numpy`
5. **Tkinter** (usually included in Python)

### You will need Pet Python 

- #### [Python 3.11.6](https://github.com/KernFerm/Py3.11.6installer)

You can install the required libraries with:

```
pip install opencv-python-headless pillow pyautogui numpy Tkinter
```

### You can use the `install_dependecies.bat` to install the dependencies needed for project

## Usage 💻

1. **Clone this repository:**
```
git clone https://github.com/kernferm/screen-recorder-app.git
```

2. **Run the app:**

```
python main.py
```

3. **Start Recording:** Hit the `Start Recording` button to begin capturing your screen.
4. **Stop Recording:** Click the `Stop Recording` button to save your recording as `screen_recording.mp4`.

## How It Works 🧐

- **Screen Recording:** The app captures screenshots using `pyautogui.screenshot()` at 60 FPS.
- **Mouse Highlighting:** A green circle 🟢 is drawn around the current mouse pointer in every frame for better visibility.
- **Saving Video:** The captured frames are saved as an MP4 file using `cv2.VideoWriter`.

-------
# Built with ❤️ by [Bubbles_The_Dev](https://github.com/kernferm)
-------
## LICENSE
### [License_Please_Read](https://github.com/KernFerm/screen-recorder-app/blob/main/LICENSE)

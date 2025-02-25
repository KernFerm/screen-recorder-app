## This project is proprietary and all rights are reserved by the author. 
## Unauthorized copying, distribution, or modification of this project is strictly prohibited. 
## Unless You have written permission from the Developer or the FNBUBBLES420 ORG.


import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import cv2
import numpy as np
import time
import threading
import pyautogui
import dxcam

ctk.set_appearance_mode("Dark")  # Set dark mode; you can change to "Light" if preferred
ctk.set_default_color_theme("blue")  # Set color theme; you can choose any theme you like

## This project is proprietary and all rights are reserved by the author. 
## Unauthorized copying, distribution, or modification of this project is strictly prohibited. 
## Unless You have written permission from the Developer or the FNBUBBLES420 ORG.

class ScreenRecorderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("BubblesTheDev Screen Recorder")
        self.geometry("400x250")

        # Variables for recording state
        self.recording = False
        self.frames = []
        self.start_time = 0
        self.file_name = "screen_recording"  # Default file name

        # Initialize BetterCam
        self.cam = dxcam.create()

        # UI Elements
        self.label = ctk.CTkLabel(self, text="BubblesTheDev Screen Recorder", font=("Arial", 14))
        self.label.pack(pady=10)

        self.filename_entry = ctk.CTkEntry(self, placeholder_text="Enter file name")
        self.filename_entry.pack(pady=10)

        self.start_button = ctk.CTkButton(self, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=10)

        self.stop_button = ctk.CTkButton(self, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

    def start_recording(self):
        file_name_entry = self.filename_entry.get().strip()
        if file_name_entry:
            self.file_name = file_name_entry
        else:
            self.file_name = "screen_recording"  # Reset to default if entry is empty

        self.recording = True
        self.frames = []
        self.start_time = time.time()
        self.start_button.configure(state=tk.DISABLED)
        self.stop_button.configure(state=tk.NORMAL)
        threading.Thread(target=self.record_screen).start()

    def stop_recording(self):
        self.recording = False
        self.start_button.configure(state=tk.NORMAL)
        self.stop_button.configure(state=tk.DISABLED)
        self.save_video()

    def record_screen(self):
        self.cam.start()
        while self.recording:
            frame = self.cam.get_latest_frame()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Get the current mouse position and draw a circle
            mouse_x, mouse_y = pyautogui.position()
            cv2.circle(frame, (mouse_x, mouse_y), 20, (0, 255, 0), 2)

            self.frames.append(frame)
            time.sleep(0.1)  # Control the frame rate
        self.cam.stop()

    def save_video(self):
        if not self.frames:
            messagebox.showerror("Error", "No frames captured!")
            return

        height, width, _ = self.frames[0].shape
        fps = len(self.frames) / (time.time() - self.start_time)
        video_path = f"{self.file_name}.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

        for frame in self.frames:
            out.write(frame)
        out.release()
        messagebox.showinfo("Success", f"Recording saved as {video_path}")

if __name__ == "__main__":
    app = ScreenRecorderApp()
    app.mainloop()

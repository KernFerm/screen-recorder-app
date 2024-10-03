import tkinter as tk
from tkinter import messagebox
import cv2
import pyautogui
from PIL import Image, ImageTk
import numpy as np
import os
import time

class ScreenRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BubblesTheDev Screen Recorder")
        self.root.geometry("400x200")
        
        # Variables for recording state
        self.recording = False
        self.frames = []
        self.start_time = 0

        # UI Elements
        self.label = tk.Label(root, text="BubblesTheDev Screen Recorder", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Recording", command=self.start_recording, width=20)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(root, text="Stop Recording", command=self.stop_recording, width=20)
        self.stop_button.pack(pady=10)
        self.stop_button.config(state=tk.DISABLED)

    def start_recording(self):
        self.recording = True
        self.frames = []
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.record_screen()

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        
        # Save the video
        self.save_video()

    def record_screen(self):
        if self.recording:
            # Capture screen using pyautogui
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Get the current mouse position
            mouse_x, mouse_y = pyautogui.position()
            
            # Draw a circle around the mouse pointer for highlighting
            cv2.circle(frame, (mouse_x, mouse_y), 20, (0, 255, 0), 2)  # Green circle with a radius of 20
            
            # Append the frame to the list of frames
            self.frames.append(frame)
            
            # Recursively call this function after 16ms (~60fps)
            self.root.after(16, self.record_screen)

    def save_video(self):
        if not self.frames:
            messagebox.showerror("Error", "No frames captured!")
            return
        
        # Get screen size from the first frame
        height, width, _ = self.frames[0].shape
        fps = len(self.frames) / (time.time() - self.start_time)
        
        # Create a VideoWriter object to save the video
        video_path = "screen_recording.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

        # Write the frames to the video file
        for frame in self.frames:
            out.write(frame)
        
        out.release()
        messagebox.showinfo("Success", f"Recording saved as {video_path}")

# Start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorderApp(root)
    root.mainloop()

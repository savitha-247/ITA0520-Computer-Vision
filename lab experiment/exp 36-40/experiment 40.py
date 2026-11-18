import cv2
import pytesseract
from tkinter import Tk, filedialog

# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Select input video
root = Tk()
root.withdraw()

video_path = filedialog.askopenfilename(
    title="Select Text Video",
    filetypes=[("MP4 Video", "*.mp4")]
)

root.destroy()

# Open video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video not found!")
else:
    frame_number = 0
    text_found = False

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Read text from one frame every 20 frames
        if frame_number % 20 == 0:

            # Convert frame to grayscale
            gray = cv2.cvtColor(
                frame, cv2.COLOR_BGR2GRAY
            )

            # Extract text using OCR
            text = pytesseract.image_to_string(gray).strip()

            if text:
                print("Detected Text:", text)
                text_found = True

        frame_number += 1

    cap.release()

    if not text_found:
        print("No visible text detected.")

    print("Text extraction completed.")

import cv2
from tkinter import Tk, filedialog

# Select input video
root = Tk()
root.withdraw()

video_path = filedialog.askopenfilename(
    title="Select Input Video",
    filetypes=[("MP4 Video", "*.mp4")]
)

root.destroy()

# Open input video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video not found!")
else:
    frames = []

    # Read all frames
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()

    if len(frames) == 0:
        print("No frames found in the video.")
    else:
        # Reverse frame order
        frames.reverse()

        height, width = frames[0].shape[:2]

        # Half FPS for slow motion
        slow_fps = fps / 2 if fps > 0 else 15

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        output = cv2.VideoWriter(
            "reverse_slow_motion.mp4",
            fourcc,
            slow_fps,
            (width, height)
        )

        # Write reversed frames
        for frame in frames:
            output.write(frame)

        output.release()

        print("Reverse slow-motion video created successfully!")
        print("Output file: reverse_slow_motion.mp4")

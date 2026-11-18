import cv2
import numpy as np
from tkinter import Tk, filedialog

# Select input image
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Background Image",
    filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
)

root.destroy()

# Read input image
image = cv2.imread(image_path)

if image is None:
    print("Image not selected or not found.")
else:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Green background range
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])

    # Detect green background
    background_mask = cv2.inRange(
        hsv, lower_green, upper_green
    )

    # Remove background
    foreground_mask = cv2.bitwise_not(background_mask)
    result = cv2.bitwise_and(
        image, image, mask=foreground_mask
    )

    # Display output
    cv2.imshow("Original Image", image)
    cv2.imshow("Background Removed", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("background_removed.png", result)

    print("Background removed successfully!")

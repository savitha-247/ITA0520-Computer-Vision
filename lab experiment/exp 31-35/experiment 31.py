import cv2
from tkinter import Tk, filedialog

# Open image selection window
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Read selected image
image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply threshold segmentation
    ret, segmented = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    # Display original image
    cv2.imshow("Original Image", image)

    # Display segmented image
    cv2.imshow("Segmented Image", segmented)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Image segmentation completed successfully!")

root.destroy()

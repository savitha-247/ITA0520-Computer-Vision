import cv2
from mtcnn import MTCNN
from tkinter import Tk, filedialog

print("Program started...")

# Select image
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Face Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

root.destroy()

if not image_path:
    print("No image selected!")
else:
    print("Image selected successfully!")

    image = cv2.imread(image_path)

    if image is None:
        print("Unable to read image!")
    else:
        print("Loading MTCNN detector...")

        detector = MTCNN()

        print("Detecting faces...")

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        faces = detector.detect_faces(rgb)

        result = image.copy()

        for face in faces:
            x, y, w, h = face["box"]

            x = max(0, x)
            y = max(0, y)

            cv2.rectangle(
                result,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                3
            )

        face_count = len(faces)

        print("Number of faces detected:", face_count)

        cv2.imshow("Faces Detected", result)

        cv2.imwrite("face_count_output.jpg", result)

        print("Output saved successfully!")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

import cv2 # a package inside the OpenCv Librery

# Initialize the camera
camera = cv2.VideoCapture(0)

# Capture a single image from the camera
_, image = camera.read()

# Save the image to a file
cv2.imwrite(".\\all-things\\camera-captured\\image.jpg", image)

# Release the camera
camera.release()

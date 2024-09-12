import cv2  # open-cv python library

# Using the Cascade Classifier with the trained model file name
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Starts your system camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

# A while loop to constantly capture images from the camera
while True:
    # Captures each frame from the video feed
    success, img = cap.read()

    # Check if the frame was captured successfully
    if not success or img is None:
        print("Error: Failed to capture image from the camera.")
        break

    # HAAR-Cascades algorithm processes gray scale images only
    # so we convert the image format from BGR to Gray
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Using cascades we attempt to detect the faces
    # NOTE: We're running detection on the GRAY image
    faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

    # If faces are found, we can draw a rectangle around them
    # for good visual representation
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

    # Show the image with the rectangles in the live feed
    cv2.imshow("Image", img)

    # Typing in the 'q' key in the keyboard will
    # kill the live camera feed window
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()

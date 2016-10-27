import cv2
import sys
import threading

cascade_path = "haarcascade_frontalface_default.xml"
frame_file_name = "saved_image"
image_count = 0
# Use Haar Cascade for face detection provided by Intel
# http://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html

face_cascade = cv2.CascadeClassifier(cascade_path)

video_capture = cv2.VideoCapture(0)

def save_frame(frame):
    global image_count
    cv2.imwrite("image"+image_count".jpg", frame)
    print("Image saved")

while True:
    # Capture frame from video capture device
    ret, frame = video_capture.read()

    #Transform captured fram to grayscale for analysis
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected_faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in detected_faces:
        # Do something with face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    # Display captured frame with detected faces
    cv2.imshow('Agentes inteligentes', frame)

    # Wait for quit command
    if cv2.waitKey(2) & 0xFF == ord('s'):
        save_frame(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
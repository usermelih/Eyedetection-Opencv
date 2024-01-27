import cv2

# The path of the xml files
eye_cascade_path = cv2.data.haarcascades + 'haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# The settings
min_neighbors = 10
scale_factor = 5

def detect_eyes(image):
    # Making grey
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Finding eyes
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors)

    # Show the eyes on the screen
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(image, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    return eyes

def are_eyes_open(eyes):
    #Counting
    num_eyes = len(eyes)

    #If there are 0 eyes
    if num_eyes == 0:
        return False

    return True

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Take the frame
    ret, frame = cap.read()

    # Detect the eyes
    eyes = detect_eyes(frame)

    # Control the them
    eyes_open = are_eyes_open(eyes)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Showing the frame that we take in line 41
    cv2.imshow('Face Detection', frame)

    # Printing the results to screen
    if eyes_open:
        cv2.putText(frame, 'Gozler Acik', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(frame, 'Gozler Kapali', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Draw a frames for eyes
    detect_eyes(frame)

    # The parameters
    cv2.putText(frame, f'minNeighbors: {min_neighbors}, scaleFactor: {scale_factor}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    # The frame for the eye detection
    cv2.imshow('Goz Kontrol', frame)

    
    # The keyboard controls
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == 82:  # upkey
        min_neighbors += 1
    elif key == 84 and min_neighbors > 1:  #downkey
        min_neighbors -= 1
    elif key == 83:  #rightkey
        scale_factor += 0.1
    elif key == 81 and scale_factor > 0.1:  #leftkey
        scale_factor -= 0.1

#close
cap.release()
cv2.destroyAllWindows()

# Note: This code will open 2 windows; one for the eyes and the other one is for the face.

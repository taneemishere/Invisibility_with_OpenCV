import cv2
import numpy as np
import time

# Capturing the background via webcam
webcam = cv2.VideoCapture(0)
time.sleep(3)
background = 0

# As the background should remain static so for the specific time we need
# to capture the background that's why using the for loop
for i in range(30):
    successful_frame, background = webcam.read()

    if not successful_frame:
        break

# Doing this because by default you'll receive the reverse order image
# as we see in the selfei cameras. So to make it as we see in the mirror
background = np.flip(background, axis=1)

# Now capturing the images until the webcam is opened
while webcam.isOpened():

    # Capturing the live stream from the webcam
    successful_frame, frame = webcam.read()

    # if the boolean successful_frame, mean if there is any error or
    # mistake break out of the loop
    if not successful_frame:
        break

    
    frame = np.flip(frame, axis=1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # value = (35, 35)

    blur = cv2.GaussianBlur(hsv, (35, 35), 0)

    # Defining lower range for red color detection.
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # Defining upper range for red color detection
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Addition of the two masks to generate the final mask.
    mask = mask1 + mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    # Replacing the pixels corresponding to the cloak with the background pixels
    frame[np.where(mask == 255)] = background[np.where(mask == 255)]

    cv2.imshow("Invisibility", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

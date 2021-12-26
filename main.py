import cv2
import numpy as np
from imutils import grab_contours
from imutils.video import VideoStream
from directkeys import A, D, Space, ReleaseKey, PressKey

cap = VideoStream(0).start()
currentKey = []

while True:
    key = False
    img = cap.read()
    img = cv2.flip(img, 1)      # Flip the image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Convert colour BGR format to HSV format
    blur_img = cv2.GaussianBlur(img, (11, 11), 0)
    colour_low = np.array([37, 89, 129])         # threshold HSV values obtained from color_select.py
    colour_upp = np.array([100, 255, 255])
    mask = cv2.inRange(blur_img, colour_low, colour_upp)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

    width = img.shape[1]
    height = img.shape[0]

    upContour = mask[0:height//2, 0:width]
    downContour = mask[3*height//4: height, 2*width//5: 3*width//5]

    cnts_up = cv2.findContours(upContour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts_up = grab_contours(cnts_up)

    cnts_down = cv2.findContours(downContour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts_down = grab_contours(cnts_down)

    if len(cnts_up) > 0:
        c = max(cnts_up, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M["m10"]/M["m00"])

        if cx < (width//2 - 35):
            PressKey(A)
            key = True
            currentKey.append(A)
        elif cx > (width//2 + 35):
            PressKey(D)
            key = True
            currentKey.append(D)
    if len(cnts_down) > 0:
        PressKey(Space)
        key = True
        currentKey.append(Space)

    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)      # Convert colour HSV format to BGR format
    img = cv2.rectangle(img, (0, 0), (width//2 - 35, height//2), (0, 255, 0), 1)
    cv2.putText(img, "LEFT", (110, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (139, 0, 0), 2)

    img = cv2.rectangle(img, (width//2 + 35, 0), (width, height//2), (0, 255, 0), 1)
    cv2.putText(img, "RIGHT", (440, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (139, 0, 0), 2)

    img = cv2.rectangle(img, (2*(width//5), 3*height//4), (3*width//5, height), (0, 255, 0), 1)
    cv2.putText(img, "NITRO", (2*(width//5) + 20, height - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (139, 0, 0), 2)

    cv2.imshow("Steering wheel", img)
    if not key and len(currentKey) != 0:
        for current in currentKey:
            ReleaseKey(current)
    if cv2.waitKey(1) == 27:        # Press ESC to quit
        break

cv2.destroyAllWindows()

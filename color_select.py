import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow("Colour Detection")


def window(x):
    pass


cv2.createTrackbar('Hue', 'Colour Detection', 0, 179, window)
cv2.createTrackbar('Saturation', 'Colour Detection', 0, 255, window)
cv2.createTrackbar('Value', 'Colour Detection', 0, 255, window)

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (480, 360))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blurred = cv2.GaussianBlur(hsv, (11, 11), 0)

    h = cv2.getTrackbarPos('Hue', 'Colour Detection')
    s = cv2.getTrackbarPos('Saturation', 'Colour Detection')
    v = cv2.getTrackbarPos('Value', 'Colour Detection')

    lower_colour = np.array([h, s, v])
    upper_colour = np.array([100, 255, 255])
    mask = cv2.inRange(hsv, lower_colour, upper_colour)
    cv2.imshow('Colour Detection', cv2.bitwise_and(img, img, mask=mask))

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

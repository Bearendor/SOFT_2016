import numpy as np
import cv2

#pathSoko = "D:\soft\level-2\\video-0.avi"

pathBera = "C:\\Users\\Marko Bera\\Desktop\\SOFT\\level-2\\video-0.avi"

cap = cv2.VideoCapture(pathBera)
while(cap.isOpened()):
    ret, frame = cap.read()


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([20, 20, 20])
    upper_green = np.array([100, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(frame, frame, mask = cv2.bitwise_not(mask))

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((2,2),np.uint8)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

    cv2.imshow('opening',opening)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
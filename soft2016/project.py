import cv2

path = "D:\soft\level-2\\video-0.avi"

cap = cv2.VideoCapture(path)
while(cap.isOpened()):
    ret, frame = cap.read()

    #cv2.imshow('res',res)
    #cv2.imshow('mask',mask)
    #cv2.imshow('gray',gray)
    #cv2.imshow('opening',opening)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
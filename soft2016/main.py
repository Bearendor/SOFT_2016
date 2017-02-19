import numpy as np
import cv2
import number_detection as nd
from cnn.mnist import Mnist

cap = cv2.VideoCapture('data/video-0.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    m = Mnist()
    sums = []

    ret, numbers = nd.find_numbers(frame)
    for number in numbers:
        sums.append(m.predict_number(number))

    print "RESULT: {}".format(sum(sums))
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# frame = cv2.imread("test/test.png")
# m = Mnist()
# sums = []
# ret, numbers = nd.find_numbers(frame)
# nd.display_image(ret)
# for number in numbers:
#     n = m.predict_number(number)
#     print n
#     sums.append(n)
#     nd.display_image(number)
# print "RESULT: {0}".format(sum(sums))

cap.release()
cv2.destroyAllWindows()
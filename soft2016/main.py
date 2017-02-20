import numpy as np
import cv2
import number_detection as nd
from cnn.mnist import Mnist
'''
ime = 'data/video-'
ext = '.avi'
xarray = ["RA 43/2012", "file"]
yarray = ["Ivan Sredojevic", "sum"]
out_path = 'result/out.txt'
out = open(out_path, 'w+')

for i in (0, 2):

    naziv = ime + `i` + ext

    xarray.append(naziv)
'''
cap = cv2.VideoCapture('data/video-7o.avi')
rez = 0
broj = 0
dodaj = 0
pomocni_broj = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    m = Mnist()
    sums = []

    ret, numbers = nd.find_numbers(frame)
    for number in numbers:
        broj = m.predict_number(number)
        sums.append(m.predict_number(number))

    if ((broj - sum(sums)) < 0):
        rez += 0
    elif (sum(sums) == 0):
        dodaj = 0
        rez += 0
    elif ((broj - sum(sums)) == 0 and dodaj == 0):
        dodaj = 1
        rez += broj
        pomocni_broj = sum(sums)

    if pomocni_broj != sum(sums) and dodaj == 1:
        rez += broj
        dodaj = 0

    print "RESULT: {}".format(sum(sums)) +"  "+"POM  "+ str(pomocni_broj)
    print "BROJ   "  + str(broj)
    print "Rezultat  " + str(rez)
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
'''    yarray.append(rez)
    cap.release()
    cv2.destroyAllWindows()

data = np.array([xarray, yarray])
data = data.T
#transponujemo niz da ga imamo u dve kolone

np.savetxt(out, data, fmt=['%s', '%s'])
'''
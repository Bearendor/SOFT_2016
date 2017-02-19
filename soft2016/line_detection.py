import cv2
import numpy as np
import math

def find_line(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 10, 50, apertureSize=3)

    lines = cv2.HoughLinesP(edges, 1, math.pi / 180, 150, minLineLength=50, maxLineGap=10)

    if lines is not None:
        for x1, y1, x2, y2 in lines[0]:
            p1 = (x1, y1)
            p2 = (x2, y2)
        return p1, p2
    else:
        return None      

    '''
    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find lines using HoughLines
    lines = cv2.HoughLines(mask, 1, np.pi / 180, 200)

    # Take 1st line
    if len(lines[0]) > 0:
        rho, theta = lines[0][0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        return (x1, y1), (x2, y2)
    else:
        print "Line NOT FOUND!"
        return None
    '''

def line_equation(x, (x1, y1), (x2, y2)):
    '''Line equation based on 2 points'''
    m = float((y1-y2))/float((x1-x2))
    return int(m*(x-x1) + y1)


def display_image(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test():
    img = cv2.imread("test/test.png")
    p1, p2 = find_line(img)
    cv2.line(img, p1, p2, (0, 0, 255), 2)
    display_image(img)
    print line_equation(2, (1, 6), (3, 2)) #expected 4


#test()
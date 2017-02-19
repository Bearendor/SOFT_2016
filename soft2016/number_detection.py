import numpy as np
import cv2
import line_detection as ld


def find_numbers(img):
    # get x1, y1, x2, y2 coordinates of blue line
    p1, p2 = ld.find_line(img)
    
    newP1 = tuple(np.subtract(p1, (0,-5)))
    newP2 = tuple(np.subtract(p2, (0,-5)))

    # convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # convert to white and black
    ret, img_bw = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

    # reduce noise using dilate and erode
    kernel = cv2.getStructuringElement(shape=0, ksize=(2, 2))
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)

    # find all contoures that are below line and add them to list
    numbers = []
    ret = img.copy()
    im2, contours, hierarchy = cv2.findContours(img_bw.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        '''and (ld.line_equation(x, p1, p2) < y)'''
        if w > 1 and h > 5:
            if ((ld.line_equation(x, p1, p2) < y) and ld.line_equation(x, newP1, newP2) > y and x > p1[0] and x < p2[0]):
                # Crop contour that contains number
                n = img_bw[y:y+h+1, x:x+w+1]
                # Reize region to match neural network input
                numbers.append(cv2.resize(n, (28, 28)))
                # Draw rectangle for testing
                cv2.rectangle(ret, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return ret, np.array(numbers)


def display_image(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test():
    img = cv2.imread("test/test.png")
    ret, numbers = find_numbers(img)
    display_image(ret)

#test()
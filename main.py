import cv2
import numpy
import Samples


if __name__ == '__main__':
    img = cv2.imread("Samples/1.jpg")
    (b, g, r) = img[0, 0]
    cv2.imshow("Display window", img)
    k = cv2.waitKey(0)

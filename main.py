from cv2 import cv2
import numpy
import Samples
from matplotlib import pyplot as plt

if __name__ == '__main__':
    img = cv2.imread("Samples/1.jpg")
    b, g, r = cv2.split(img)
    rgb_img = cv2.merge([r, g, b])

    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    b, g, r = cv2.split(dst)
    rgb_dst = cv2.merge([r, g, b])
    plt.subplot(211), plt.imshow(rgb_img)
    plt.subplot(212), plt.imshow(rgb_dst)
    plt.show()
    cv2.imshow("Display window", img)


    k = cv2.waitKey(0)

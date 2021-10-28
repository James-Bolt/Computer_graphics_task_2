from cv2 import cv2
import numpy
import Samples
from matplotlib import pyplot as plt

def  NonLocalMeans(img):
    b, g, r = cv2.split(img)
    rgb_img = cv2.merge([r, g, b])

    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    b, g, r = cv2.split(dst)
    rgb_dst = cv2.merge([r, g, b])
    plt.subplot(211), plt.imshow(rgb_img)
    plt.subplot(212), plt.imshow(rgb_dst)

if __name__ == '__main__':
    img = cv2.imread("Samples/1.jpg")
    NonLocalMeans(img)
    plt.show()

    k = cv2.waitKey(0)

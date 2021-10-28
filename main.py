from cv2 import cv2
import numpy as np
import Samples
from matplotlib import pyplot as plt

def NonLocalMeans(img):
    b, g, r = cv2.split(img)
    rgb_img = cv2.merge([r, g, b])
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    b, g, r = cv2.split(dst)
    rgb_dst = cv2.merge([r, g, b])
    plt.subplot(211), plt.imshow(rgb_img)
    plt.subplot(212), plt.imshow(rgb_dst)


def makeMask(img):
    image = cv2.imread(img)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    image_erode = cv2.erode(image, kernel)
    hsv_img = cv2.cvtColor(image_erode, cv2.COLOR_BGR2HSV)
    markers = np.zeros((image.shape[0], image.shape[1]), dtype=" int32 ")
    markers[90: 140, 90: 140] = 255
    markers[236: 255, 0: 20] = 1
    markers[0: 20, 0: 20] = 1
    markers[0: 20, 236: 255] = 1
    markers[236: 255, 236: 255] = 1
    leafs = cv2.watershed(image_erode, markers)
    healthy_part = cv2.inRange(hsv_img, (36, 25, 25), (86, 255, 255))
    ill_part = leafs - healthy_part
    mask = np.zeros_like(image, np.uint8)
    mask[leafs > 1] = (255, 0, 255)
    mask[ill_part > 1] = (0, 0, 255)
    return mask

if __name__ == '__main__':
    img = cv2.imread("Samples/1.jpg")
    NonLocalMeans(img)
    plt.show()
    k = cv2.waitKey(0)

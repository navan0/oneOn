import cv2
import os

w1 = 100
h1 = 100
TARGER_DIR = '/home/navaneeth/work/oneon/detected'
epoches = 3
image = cv2.imread("/home/navaneeth/work/oneon/test.jpg")
(h, w) = image.shape[:2]
center = (w / 2, h / 2)


def rotate(image):
    M = cv2.getRotationMatrix2D(center, 180, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    rotate_imgs = os.path.join(TARGER_DIR, "rota_" + str(i) + ".png")
    cv2.imwrite(rotate_imgs, rotated)


def resize(image):
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    resiz_imgs = os.path.join(TARGER_DIR, "resiz_" + str(i) + ".png")
    cv2.imwrite(resiz_imgs, resized)


for i in range(epoches):
    r = h/image.shape[1]
    dim = (w, int(image.shape[0]*r))
    rotate(image)
    resize(image)
    w1 = w1+4
    h1 = h1+4
    i = i+1

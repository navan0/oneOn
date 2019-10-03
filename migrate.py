import cv2
import os
from PIL import Image
import argparse
import numpy as np

TARGER_DIR = '/home/navaneeth/work/oneon/detected'
epoches = int(10)
h1 = 100
w1 = 100
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


class Basic:
    def __init__(self):
        basewidth = 600
        self.image0 = Image.open('/home/navaneeth/work/oneon/test.jpg')
        self.wpercent = (basewidth / float(self.image0.size[0]))
        self.hsize = int((float(self.image0.size[1]) * float(self.wpercent)))
        self.image0 = self.image0.resize((basewidth, self.hsize), Image.ANTIALIAS)
        self.image0.save('resized_image.jpg')
        self.image = cv2.imread("resized_image.jpg")

    def rotate(self):
        (h, w) = self.image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, 180, 1.0)
        rotated = cv2.warpAffine(self.image, M, (w+i, h+i))
        rotate_imgs = os.path.join(TARGER_DIR, "rota_" + str(i) + ".png")
        cv2.imwrite(rotate_imgs, rotated)
        return 0

    def resize(self):
        r = h1/self.image.shape[1]
        dim = (w1, int(self.image.shape[0]*r))
        resized = cv2.resize(self.image, dim, interpolation=cv2.INTER_AREA)
        resiz_imgs = os.path.join(TARGER_DIR, "resiz_" + str(i) + ".png")
        cv2.imwrite(resiz_imgs, resized)
        return 0


for i in range(epoches):

    p1 = Basic()
    p1.rotate()
    p1.resize()
    h1 = h1*2
    w1 = w1*2
    i = i+1

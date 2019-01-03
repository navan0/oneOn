import cv2
import os
from PIL import Image
import argparse
import numpy as np
from gan import paste_image
# from gan import blend

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--epoches', help='add number as epoches . eg: python -e 5', required=True)
args = parser.parse_args()
# print(args.epoches)
TARGER_DIR = './detected'
basewidth = 600
image0 = Image.open('./test.jpg')
wpercent = (basewidth / float(image0.size[0]))
hsize = int((float(image0.size[1]) * float(wpercent)))
image0 = image0.resize((basewidth, hsize), Image.ANTIALIAS)
image0.save('resized_image.jpg')
image = cv2.imread("./resized_image.jpg")
epoches = int(args.epoches)
h1 = 100
w1 = 100
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


def rotate(image):
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, 180, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    rotate_imgs = os.path.join(TARGER_DIR, "rota_" + str(i) + ".png")
    cv2.imwrite(rotate_imgs, rotated)
    return 0


def resize(image):
    r = h1/image.shape[1]
    dim = (w1, int(image.shape[0]*r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    resiz_imgs = os.path.join(TARGER_DIR, "resiz_" + str(i) + ".png")
    cv2.imwrite(resiz_imgs, resized)
    return 0


def image_b(image):
    for i in range(epoches):
        blur = cv2.blur(image, (i+4, 5))
        blur_imgs = os.path.join(TARGER_DIR, "blur_" + str(i) + ".png")
        median = cv2.medianBlur(image, 5)
        mblur_imgs = os.path.join(TARGER_DIR, "mblur_" + str(i) + ".png")
        bilateral = cv2.bilateralFilter(image, i+4, i+75, i+75)
        bblur_imgs = os.path.join(TARGER_DIR, "bblur_" + str(i) + ".png")
        gaussian = cv2.GaussianBlur(image, (5, 5), 0)
        gblur_imgs = os.path.join(TARGER_DIR, "gblur_" + str(i) + ".png")
        cv2.imwrite(blur_imgs, blur)
        cv2.imwrite(mblur_imgs, median)
        cv2.imwrite(bblur_imgs, bilateral)
        cv2.imwrite(gblur_imgs, gaussian)
    return 0


def image_grey(image):
    for i in range(epoches):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resiz_imgs = os.path.join(TARGER_DIR, "grey_" + str(i) + ".png")
        cv2.imwrite(resiz_imgs, gray_image)
    return 0


def detect_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for i in range(epoches):
        for (x, y, w, h) in faces:
            roi_color = image[y:y+h, x:x+w]
            face_ = os.path.join(TARGER_DIR, "face_" + str(i) + ".png")
        cv2.imwrite(face_, roi_color)
    return 0


def detect_box(image, cropIt=True):
    image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    image_y = np.zeros(image_yuv.shape[0:2], np.uint8)
    image_y[:, :] = image_yuv[:, :, 0]
    image_blurred = cv2.GaussianBlur(image_y, (3, 3), 0)
    edges = cv2.Canny(image_blurred, 100, 300, apertureSize=3)
    _, contours, _ = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    imo_ = os.path.join(TARGER_DIR, "cont_" + str(i) + ".png")
    cv2.imwrite(imo_, edges)
    return 0


def cont_(image):
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    imo = cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    imo_ = os.path.join(TARGER_DIR, "cont_" + str(i) + ".png")
    cv2.imwrite(imo_, imo)
    return 0


for i in range(epoches):
    paste_image(image)
    detect_face(image)
    rotate(image)
    resize(image)
    image_b(image)
    image_grey(image)
    cont_(image)
    detect_box(image)
    # blend(image)

    h1 = h1*2
    w1 = w1*2
    i = i+1

os.system("rm ./resized_image.jpg")
# delete the resized image

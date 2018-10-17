import cv2
import os
import PIL
from PIL import Image
TARGER_DIR = '/home/navaneeth/work/oneon/detected'
basewidth = 600
image0 = Image.open('/home/navaneeth/work/lobster.jpg')
wpercent = (basewidth / float(image0.size[0]))
hsize = int((float(image0.size[1]) * float(wpercent)))
image0 = image0.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
image0.save('resized_image.jpg')
image = cv2.imread("/home/navaneeth/work/oneon/resized_image.jpg")
epoches = 1
h1 = 100
w1 = 100


def rotate(image):
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, 180, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    rotate_imgs = os.path.join(TARGER_DIR, "rota_" + str(i) + ".png")
    cv2.imwrite(rotate_imgs, rotated)


def resize(image):
    r = h1/image.shape[1]
    dim = (w1, int(image.shape[0]*r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    resiz_imgs = os.path.join(TARGER_DIR, "resiz_" + str(i) + ".png")
    cv2.imwrite(resiz_imgs, resized)


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


for i in range(epoches):
    rotate(image)
    resize(image)
    image_b(image)
    h1 = h1*2
    w1 = w1*2
    i = i+1

os.system("rm /home/navaneeth/work/oneon/resized_image.jpg")
# deleted the resized image

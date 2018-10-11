import cv2
import os

w = 100
h = 100
epoches = 1000
image = cv2.imread("/home/navaneeth/work/oneon/test.jpg")
for i in range(epoches):
    r = h/image.shape[1]
    dim = (w, int(image.shape[0]*r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    # cropped = image[70+w:100, 200+h:220]
    manip_imgs = os.path.join("manip_" + str(i) + ".png")
    # crop_imgs = os.path.join("crop_" + str(i) + ".png")
    cv2.imwrite(manip_imgs, resized)
    # cv2.imwrite(crop_imgs, cropped)
    i = i+1
    w = w+4
    h = h+4

cv2.waitKey(0)

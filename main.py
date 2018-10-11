import cv2
import os

w1 = 100
h1 = 100
epoches = 1000
image = cv2.imread("/home/navaneeth/work/oneon/test.jpg")
(h, w) = image.shape[:2]
center = (w / 2, h / 2)
for i in range(epoches):
    r = h/image.shape[1]
    dim = (w, int(image.shape[0]*r))
    M = cv2.getRotationMatrix2D(center, 180, 1.0)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    # cropped = image[70+w:100, 200+h:220]
    rotated = cv2.warpAffine(image, M, (w, h))
    manip_imgs = os.path.join("manip_" + str(i) + ".png")
    rotate_imgs = os.path.join("rota_" + str(i) + ".png")
    # crop_imgs = os.path.join("crop_" + str(i) + ".png")
    cv2.imwrite(manip_imgs, resized)
    cv2.imwrite(rotate_imgs, rotated)
    # cv2.imwrite(crop_imgs, cropped)
    i = i+1
    w1 = w1+4
    h1 = h1+4

cv2.waitKey(0)

# rotate the image by 180 degrees
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

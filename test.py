import cv2
import numpy as np
import os
TARGER_DIR = '/home/navaneeth/work/oneon/detected'

image = cv2.imread("/home/navaneeth/work/oneon/test2.png")
debug_mode = True
i=1

def detect_box(image, cropIt=True):
	image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
	image_y = np.zeros(image_yuv.shape[0:2], np.uint8)
	image_y[:, :] = image_yuv[:, :, 0]
	image_blurred = cv2.GaussianBlur(image_y, (3, 3), 0)
	edges = cv2.Canny(image_blurred, 100, 300, apertureSize=3)
	_, contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	imo_ = os.path.join(TARGER_DIR, "cont_" + str(i) + ".png")
	cv2.imwrite(imo_,image)



detect_box(image)

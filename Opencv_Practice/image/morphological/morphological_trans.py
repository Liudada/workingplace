import cv2
import numpy as np

i = 0
def show(img):
	global i
	i += 1
	cv2.imshow(str(i), img)
	cv2.waitKey(0)

img = cv2.imread('../data/j.png', 0)
opening = cv2.imread('../data/opening.png', 0)
closing = cv2.imread('../data/closing.png', 0)

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(closing, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

show(img)
#show(erosion)
#show(dilation)
#show(opening)
#show(closing)
#show(gradient)
#show(tophat)
#show(blackhat)
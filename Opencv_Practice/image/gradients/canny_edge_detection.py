import cv2
import numpy as np

def nothing(x):
	pass

img = cv2.imread('../data/dave.png', 0)
cv2.namedWindow('edges')
cv2.createTrackbar('min', 'edges', 0, 1000, nothing)
cv2.createTrackbar('max', 'edges', 0, 1000, nothing)

while 1:
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	mi = cv2.getTrackbarPos('min', 'edges')
	mx = cv2.getTrackbarPos('max', 'edges')
	edges = cv2.Canny(img, mi, mx)
	cv2.imshow('edges', edges)

cv2.destroyAllWindows()
import numpy as np
import cv2

im = cv2.imread('../data/114-4-007.tif')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 128, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('image', image)
cv2.waitKey(0)
img = cv2.drawContours(im, contours, -1, (0,0,255), 1)
cv2.imshow('contours', img)
cv2.waitKey(0)
print(hierarchy)
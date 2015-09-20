import cv2
import numpy as np

img = cv2.imread('../data/opencv_logo.png')

#blur = cv2.blur(img, (15,15))
#blur = cv2.GaussianBlur(img, (15,15), 0)
blur = cv2.bilateralFilter(img, 9, 75, 75)
median = cv2.medianBlur(img, 15)

cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.imshow('Blurred', median)
cv2.waitKey(0)
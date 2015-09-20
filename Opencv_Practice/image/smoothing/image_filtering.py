import cv2
import numpy as np

img = cv2.imread('../data/opencv_logo.png')

kernel = np.ones((15,15), np.float32) / 15**2
dst = cv2.filter2D(img, -1, kernel)

cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.imshow('Averaging', dst)
cv2.waitKey(0)
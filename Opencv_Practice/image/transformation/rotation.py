import cv2
import numpy as np

img = cv2.imread('../data/bg02.png', 0)
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, M, (cols,rows))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imshow('rot', dst)
cv2.waitKey(0)
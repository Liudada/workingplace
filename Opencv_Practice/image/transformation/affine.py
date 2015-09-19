import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/opencv_logo.png')
rows, cols, ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
for pt in pts1:
	img = cv2.circle(img,tuple(pt),10,(255,255,255),-1)

M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img, M, (cols,rows))
for pt in pts2:
	dst = cv2.circle(dst,tuple(pt),10,(255,255,255),-1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imshow('dst', dst)
cv2.waitKey(0)
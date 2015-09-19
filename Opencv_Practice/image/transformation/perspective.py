import cv2
import numpy as np

img = cv2.imread('../data/opencv_logo.png')
rows, cols, ch = img.shape

pts1 = np.float32([[0,0],[cols,0],[200,rows],[cols-200,rows]])
pts2 = np.float32([[0,0],[cols,0],[0,rows],[cols,rows]])
for pt in pts1:
	img = cv2.circle(img,tuple(pt),10,(128,128,128),-1)

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img, M, (cols,rows))
for pt in pts2:
	dst = cv2.circle(dst,tuple(pt),10,(128,128,128),-1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imshow('dst', dst)
cv2.waitKey(0)
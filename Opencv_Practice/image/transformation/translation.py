import cv2
import numpy as np

img = cv2.imread('../data/opencv_logo.png')
rows, cols = img.shape[:2]

M = np.float32([[1,0,200],[0,1,50]])
dst = cv2.warpAffine(img, M, (cols+200,rows+50))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
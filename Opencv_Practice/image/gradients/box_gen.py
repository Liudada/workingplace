import cv2
import numpy as np

img = np.zeros((600, 800), dtype='uint8')
for i in range(150, 450):
	for j in range(200, 600):
		img[i][j] = 255

cv2.imshow('box', img)
cv2.imwrite('box.png', img)
cv2.waitKey(0)
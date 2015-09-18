import cv2
import numpy as np

img = np.ones((600, 800), dtype='uint8') * 50
for i in range(150, 450):
	for j in range(200, 600):
		img[i][j] = 127

gauss = np.random.normal(0, 25, (600,800))
gauss = gauss.reshape(600,800)
noise = np.uint8(abs(img + gauss))

cv2.imshow('noise', noise)
cv2.imwrite('noisy2.png', noise)
cv2.waitKey(0)
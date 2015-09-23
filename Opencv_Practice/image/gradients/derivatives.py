import cv2
import numpy as np

i = 0
def show(img):
	global i
	i += 1
	cv2.imshow(str(i), img)
	cv2.waitKey(0)

img = cv2.imread('../data/dave.png', 0)
box = cv2.imread('./box.png', 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
sobelx64f = np.absolute(cv2.Sobel(box, cv2.CV_64F, 1, 0, ksize=5))
sobelx8u = cv2.Sobel(box, cv2.CV_8U, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)

show(img)
show(laplacian)
show(sobelx)
show(sobely)
show(sobelx64f)
show(sobelx8u)
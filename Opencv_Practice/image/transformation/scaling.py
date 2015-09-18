import cv2
import numpy as np

img = cv2.imread('../data/Eva_46.png')

res = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)
cv2.imshow('method1', res)
cv2.waitKey(0)

height, width = img.shape[:2]
res = cv2.resize(img, (5*width, 5*height), interpolation=cv2.INTER_CUBIC)
cv2.imshow('method2', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
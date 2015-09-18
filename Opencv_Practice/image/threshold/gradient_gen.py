import cv2
import numpy as np

img = np.uint8(np.arange(256*256).reshape(256,256) % 256)
cv2.imwrite('gradient.png', img)
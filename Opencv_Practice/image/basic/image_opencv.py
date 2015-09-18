import numpy as np
from cv2 import *
from matplotlib import pyplot as plt

img = imread('../data/miku_kimono.jpg')
for i in range(len(img)):
	for j in range(len(img[0])):
		img[i][j][0],img[i][j][2] = img[i][j][2],img[i][j][0]
plt.imshow(img, interpolation='bicubic')
plt.xticks([])
plt.yticks([])
plt.show()
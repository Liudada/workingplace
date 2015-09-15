import numpy as np
from cv2 import *

img = np.zeros((512,512,3), np.uint8)
for i in range(512):
	for j in range(512):
		img[i][j] = [185,128,41]

centers = []
for angle in [np.pi*2/3,np.pi*4/3,0]:
	centers.append((int(256+np.sin(angle)*128),int(256-np.cos(angle)*128)))
for i in range(3):
	color = [0,0,0]
	color[i] = 255
	if i == 0:
		img = ellipse(img,centers[i],(102,102),300,0,300,tuple(color),-1)
	else:
		img = ellipse(img,centers[i],(102,102),120*(i-1),0,300,tuple(color),-1)
	img = circle(img,centers[i],40,(185,128,41),-1)

imshow('drawing',img)
if waitKey(0) & 0xFF == 27:
	destroyAllWindows()
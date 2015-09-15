from cv2 import *
import numpy as np

img = imread('114-4-007.tif')
gray,gray,gray = split(img)

for i in range(len(gray)):
	if 0 in gray[i]:
		break
gray = gray[0:i]

for i in range(len(gray)):
	for j in range(len(gray[0])):
		if gray.item(i,j) > 135:
			gray.itemset((i,j),255)
		else:
			gray.itemset((i,j),0)

print(gray)

imshow('image',gray)
waitKey(0)
from cv2 import *
import numpy as np

img1 = imread('../data/miku_kimono.jpg')
img2 = imread('../data/bg02.png')
img3 = imread('../data/bg01.jpg')

def nothing(x):
	pass

namedWindow('image')
createTrackbar('weight1','image',0,100,nothing)
createTrackbar('weight2','image',0,100,nothing)

while(1):
	weight1 = getTrackbarPos('weight1','image')
	weight2 = getTrackbarPos('weight2','image')
	alpha1 = round(0.01*weight1,2)
	alpha2 = round(0.01*weight2,2)
	img = addWeighted(img1,alpha1,img2,1-alpha1,0)
	img = addWeighted(img,alpha2,img3,1-alpha2,0)
	imshow('image',img)
	k = waitKey(1) & 0xFF
	if k == 27:
		break
destroyAllWindows()
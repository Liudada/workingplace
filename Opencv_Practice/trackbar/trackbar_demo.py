from cv2 import *
import numpy as np

def nothing(x):
	pass

img = np.zeros((300,512,3),np.uint8)
namedWindow('image')

createTrackbar('R','image',0,255,nothing)
createTrackbar('G','image',0,255,nothing)
createTrackbar('B','image',0,255,nothing)

switch = '0 : OFF \n1 : ON'
createTrackbar(switch,'image',0,1,nothing)

while(1):
	imshow('image',img)
	k = waitKey(1) & 0xFF
	if k == 27:
		break
	r = getTrackbarPos('R','image')
	g = getTrackbarPos('G','image')
	b = getTrackbarPos('B','image')
	s = getTrackbarPos(switch,'image')
	if s == 0:
		img[:] = 0
	else:
		img[:] = [b,g,r]
destroyAllWindows()
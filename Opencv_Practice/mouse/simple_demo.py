from cv2 import *
import numpy as np

def draw_circle(event,x,y,flags,param):
	if event == EVENT_LBUTTONDBLCLK:
		circle(img,(x,y),100,(255,0,0),-1)

img = np.zeros((512,512,3),np.uint8)
namedWindow('image')
setMouseCallback('image',draw_circle)

while(1):
	imshow('image',img)
	if waitKey(20) & 0xFF == 27:
		break
destroyAllWindows()
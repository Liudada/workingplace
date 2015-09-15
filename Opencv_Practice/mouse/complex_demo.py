from cv2 import *
import numpy as np

drawing = False
mode = True
ix, iy = -1, -1
nx, ny = -1, -1
finished = []

def draw_circle(event,x,y,flags,param):
	global ix, iy, nx, ny, drawing, mode, finished
	if event == EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y
	elif event == EVENT_MOUSEMOVE:
		if drawing == True:
			if mode == True:
				rectangle(img,(ix,iy),(nx,ny),(0,0,0),1)
				for fin in finished:
					rectangle(img,fin[0],fin[1],(0,255,0),1)
				rectangle(img,(ix,iy),(x,y),(0,255,0),1)
				nx, ny = x, y
			else:
				circle(img,(x,y),5,(0,0,255),-1)
	elif event == EVENT_LBUTTONUP:
		drawing = False
		if mode == True:
			rectangle(img,(ix,iy),(x,y),(0,255,0),1)
		else:
			circle(img,(x,y),5,(0,0,255),-1)
		nx, ny = -1, -1
		finished.append([(ix,iy),(x,y)])

img = np.zeros((512,512,3),np.uint8)
namedWindow('image')
setMouseCallback('image',draw_circle)
while(1):
	imshow('image',img)
	k = waitKey(20) & 0xFF
	if k == ord('m'):
		mode = not mode
	elif k == 27:
		break
destroyAllWindows()
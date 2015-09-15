from cv2 import *
import numpy as np

drawing = False
ix, iy = -1, -1
path = []
mode = 'curve'

def nothing(x):
	pass

def draw_circle(event,x,y,flags,param):
	global drawing, r, g, b, radius, ix, iy, path
	if event == EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y
	elif event == EVENT_MOUSEMOVE:
		if mode == 'curve':
			if drawing == True:
				short = int(max(abs(ix-x),abs(iy-y))[0][0])
				for i in range(1,short+1):
					circle(img,(ix+int((x-ix)/short*i),iy+int((y-iy)/short*i)),radius,(b,g,r),-1)
					path.append(((ix+int((x-ix)/short*i),iy+int((y-iy)/short*i)),radius,(b,g,r)))
			else:
				circle(img,(ix,iy),radius,(0,0,0),-1)
				for pt in path:
					circle(img,pt[0],pt[1],pt[2],-1)
				circle(img,(x,y),radius,(b,g,r),-1)
			ix, iy = x, y
		elif mode == 'straight':
			if drawing == True:
				if abs(x-ix) >= abs(y-iy):
					begin = int(min(x,ix)[0][0])
					end = int(max(x,ix)[0][0]) + 1
					for i in range(begin,end):
						circle(img,(i,iy),radius,(b,g,r),-1)
						path.append(((i,iy),radius,(b,g,r),-1))
				else:
					begin = int(min(y,iy)[0][0])
					end = int(max(y,iy)[0][0]) + 1
					for i in range(begin,end):
						circle(img,(ix,i),radius,(b,g,r),-1)
						path.append(((ix,i),radius,(b,g,r),-1))
	elif event == EVENT_LBUTTONUP:
		drawing = False
		circle(img,(x,y),radius,(b,g,r),-1)
		path.append(((x,y),radius,(b,g,r)))

img = np.zeros((720,1280,3),np.uint8)
namedWindow('image')
setMouseCallback('image',draw_circle)
createTrackbar('R','image',0,255,nothing)
createTrackbar('G','image',0,255,nothing)
createTrackbar('B','image',0,255,nothing)
createTrackbar('brush radius','image',0,30,nothing)

while(1):
	imshow('image',img)
	k = waitKey(1) & 0xFF
	if k == 27:
		break
	elif k == ord('c'):
		img = np.zeros((720,1280,3),np.uint8)
		path = []
	elif k == ord('s'):
		if mode == 'curve':
			mode = 'straight'
		elif mode == 'straight':
			mode = 'curve'
	r = getTrackbarPos('R','image')
	g = getTrackbarPos('G','image')
	b = getTrackbarPos('B','image')
	radius = getTrackbarPos('brush radius','image')
destroyAllWindows()
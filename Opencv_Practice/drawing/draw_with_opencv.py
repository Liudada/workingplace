import numpy as np
from cv2 import *

img = np.zeros((512,512,3), np.uint8)

img = line(img,(0,0),(511,511),(255,0,0),5)
img = rectangle(img,(384,0),(510,128),(0,255,0),3)
img = circle(img,(447,63),63,(0,0,255),-1)
img = ellipse(img,(256,256),(100,50),0,0,180,(255,255,0),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = polylines(img,[pts],True,(0,255,255))

font = FONT_HERSHEY_SIMPLEX
putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,LINE_AA)

imshow('drawing',img)
if waitKey(0) & 0xFF == 27:
	destroyAllWindows()
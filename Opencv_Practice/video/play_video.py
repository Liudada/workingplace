import numpy as np
from cv2 import *

cap = VideoCapture('Blizzard.avi')

while(cap.isOpened()):
	ret, frame = cap.read()
	frame = cvtColor(frame, COLOR_BGR2GRAY)
	imshow('frame',frame)
	if waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
destroyAllWindows()
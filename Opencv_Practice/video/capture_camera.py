import numpy as numpy
from cv2 import *

cap = VideoCapture(0)
ret = cap.set(3,1920*2)
ret = cap.set(4,1080*2)

while True:
	ret, frame = cap.read()
	imshow('frame',frame)
	if waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
destroyAllWindows()
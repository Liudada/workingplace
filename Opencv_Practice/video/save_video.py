import numpy as np
from cv2 import *

cap = VideoCapture(0)

fourcc = VideoWriter_fourcc(*'XVID')
out = VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		out.write(frame)
		imshow('frame',frame)
		if waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
out.release()
destroyAllWindows()
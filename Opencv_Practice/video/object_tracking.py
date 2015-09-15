import cv2
import numpy as np

cap = cv2.VideoCapture(0)

"""while 1:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower = np.array([[110,50,50],[50,110,50],[50,50,110]])
	upper = np.array([[130,255,255],[255,130,255],[255,255,130]])
	masks = np.array([cv2.inRange(hsv, lower[i], upper[i]) for i in range(3)])
	mask = sum(masks)
	res = cv2.bitwise_and(frame, frame, mask=mask)
	cv2.imshow('res', res)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break"""

while 1:
	_, frame = cap.read()
	lower = np.array([[100,0,0],[0,100,0],[0,0,100]])
	upper = np.array([[255,100,100],[100,255,100],[100,100,255]])
	masks = np.array([cv2.inRange(frame, lower[i], upper[i]) for i in range(3)])
	mask = sum(masks)
	res = cv2.bitwise_and(frame, frame, mask=mask)
	cv2.imshow('res', res)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
import cv2
import numpy as np

higher_reso = cv2.imread('../data/bg02.png')
lower_reso = cv2.pyrDown(higher_reso)
higher_reso2 = cv2.pyrUp(lower_reso)
cv2.imshow('higher', higher_reso2)
cv2.waitKey(0)
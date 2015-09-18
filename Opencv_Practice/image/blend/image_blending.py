from cv2 import *
import numpy as np

img1 = imread('../data/miku_kimono.jpg')
img2 = imread('../data/bg02.png')

dst = addWeighted(img1,0.5,img2,0.5,0)

imshow('dst',dst)
waitKey(0)
destroyAllWindows()
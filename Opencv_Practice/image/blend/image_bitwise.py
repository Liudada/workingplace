from cv2 import *
import numpy as np

img1 = imread('../data/miku_kimono.jpg')
img2 = imread('../data/Eva_46.png')

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cvtColor(img2,COLOR_BGR2GRAY)
ret, mask = threshold(img2gray,80,255,THRESH_BINARY)
mask_inv = bitwise_not(mask)

img1_bg = bitwise_and(roi,roi,mask=mask)
img2_fg = bitwise_and(img2,img2,mask=mask_inv)

dst = add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

imshow('mask',mask)
waitKey(0)
imshow('mask_inv',mask_inv)
waitKey(0)
imshow('res',img1)
waitKey(0)
destroyAllWindows()
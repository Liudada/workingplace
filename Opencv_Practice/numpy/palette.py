from numpy import *
from cv2 import *

palette = zeros(256**3*3).reshape(256,256,256,3)
for i in range(256):
	for j in range(256):
		for k in range(256):
			palette[i,j,k,0] = i
			palette[i,j,k,1] = j
			palette[i,j,k,2] = k
palette.resize(16**3,16**3,3)
print(palette)
imshow('image',uint8(palette))
waitKey(0)
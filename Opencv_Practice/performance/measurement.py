from cv2 import *
from time import time
import numpy as np

img1 = imread('../image/bg02.png')

t = np.zeros(10)
for i in range(10):
	t1 = time()
	img1 = medianBlur(img1,49)
	t2 = time()
	t[i] = t2 - t1
mx = t.max()
best = np.arange(10)[t==mx]
print(t)
avg = sum(t) / 10

print("10 loops, best of %d: %f ms per loop" % (best[0], avg*10))
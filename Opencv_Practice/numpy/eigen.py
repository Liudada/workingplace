from numpy import *
from numpy.linalg import *

j = array([[0.0,-1.0],[1.0,0.0]])
eigen = eig(j)

for i in range(len(eigen[0])):
	print(eigen[0][i] * eigen[1][:,i])
	print(dot(j,eigen[1][:,i]))
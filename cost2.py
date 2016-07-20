import numpy as np
import math 

def valuee(X,p,y): 

	m = len(X.index)

	X = np.array(X)

	J = 0

	for i in xrange(m):
		xi = X[i,:]
		J = J - ( y[i]*math.log(p[i]) + (1-y[i])*math.log(1-p[i]) )/m

	return J 
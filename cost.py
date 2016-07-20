import numpy as np
import math

def logistic(t):
    return 1.0 / ( 1 + math.exp((-1.0)*t) ) 

def valuee(X,y,theta): 

	m = len(X.index)

	X = np.array(X)

	J = 0

	for i in xrange(m):
		xi = X[i,:]
		h = logistic( np.dot(xi,theta) )
		J = J - ( y[i]*math.log(h) + (1-y[i])*math.log(1-h) )/m

	return J 

	 


	 
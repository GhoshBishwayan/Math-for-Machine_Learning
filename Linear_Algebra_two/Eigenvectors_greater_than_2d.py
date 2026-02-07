'''
While plotting gets trickier in higher-dimensional spaces, 
we can nevertheless find and use eigenvectors with more than two dimensions. 

Here's a 3D example (there are three dimensions handled over three rows):
'''

import numpy as np

X = np.array([[25, 2, 9], [5, 26, -5], [3, 7, -1]])

lambdas_X, V_X = np.linalg.eig(X)

print(lambdas_X, end="\n")

print(V_X)

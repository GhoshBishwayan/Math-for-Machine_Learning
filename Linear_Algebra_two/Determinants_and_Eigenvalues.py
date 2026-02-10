'''
Reln. between Determinants and Eigenvalues

Det(X) = product of all Eigenvalues of X 
'''

import numpy as np

X = np.array([[1,2,4],[2,-1,3],[0,5,1]])


X_det = np.linalg.det(X)

lambdas, V =  np.linalg.eig(X)

X_eigen_product = np.prod(lambdas)

print("Determinants: ", X_det)
print("Eigenvalues Product: ", X_det)
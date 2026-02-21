'''
Even if a matrix can't be inverted, solving equation may still be possible by other means 
Such 'other mean' 

Moore-Pensore Pseudoinverse


A^+ = V(D^+)U.T
 
where, U,D,V are SVD of A
D^+ =  (D with reciprocal of all-non zero elements)^T

'''
import numpy as np

A = np.array([[-1,2],[3,-2],[5,7]])

# svd
U, d, VT = np.linalg.svd(A)

# V
V = VT.T

# UT

UT = U.T

# To get D^T first need to do 
D = np.diag(d)

# then we would take the transpose of the resulting matrix
# Because D is a diagonal matrix, this can be done in a single step by nverting D:
Dinv = np.linalg.inv(D)

# D^+ must have the same dimensions as A^T in order for V(D^+)U.T matrix multiplication to be possible
Dplus = np.concatenate((Dinv, np.array([[0,0]]).T), axis=1)

# A^+

Aplus = np.dot(V, np.dot(Dplus, UT))

print("Moore-Penrose Pseudoinverse : ")
print(Aplus)

# Using Numpy .pinv()

Aplus_np = np.linalg.pinv(A)

print("Moore-Penrose Pseudoinverse (Numpy in-bult) : ")
print(Aplus_np)


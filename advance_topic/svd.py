'''
Singular Value Decomposition (SVD)

SVD of matrix A is 

A = UDV^T

U is an orthogonal m*m matrix; 
its columns are the left-singular vectors of A

V is an orthogonal n*n matrix;
its columns are the right-singular vectors of A

D is a diagonal m*n matrix;
elements along its diagonal are the singular values of A 
'''

import numpy as np 

A = np.array([[-1, 2], [3, -2], [5, 7]])

U, d, VT = np.linalg.svd(A)

# print(U)
# print(d)
# print(VT)

d_diag = np.diag(d)

'''
D must have the same dimensions as A for UDV^T matrix multiplication to be possible
'''

D = np.concatenate((d_diag, [[0,0]]), axis=0)

A_svd = np.dot(U, (np.dot(D, VT)))  # returns in float type

print("Original Matrix: ")
print(A)

print("SVD: ")
print(A_svd)


'''
SVD and eigendecomposition are closely related to each other:

Left-singular vectors of A = eigenvectors of A(A^T)
Right-singular vectors of A = eigenvectors of (A^T)A
Non-zero singular velues of A = square roots of eigenvalues of A(A^T) = square roots of eigenvalues of (A^T)A

'''
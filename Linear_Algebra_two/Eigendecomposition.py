'''
The eigendecomposition of some matrix A is

A=QΛQ^-1

where Q is the concatenation of all the eigenvectors of A, 
and Λ is the diagonal matrix diag(λ) - λ is the Eigenvalue .

Note that the convention is to arrange the lambda values in descending order,
as a result, 
the first eigenvalue(and its associated eigenvector) mayy be a primary characteristic of the matrix A.
'''

import numpy as np

A = np.array([[4,2],[-5,-3]])

A_eigval, Q = np.linalg.eig(A)

Qinv = np.linalg.inv(Q)

A_eigval_diag = np.diag(A_eigval)

# Confirm that A=QΛQ^-1

A_eig_decom = np.dot(Q, (np.dot(A_eigval_diag, Qinv)))

print(A_eig_decom) # which equals to A

'''
Eigendecomposition is not possible with all matrices. And in some cases where it is possible, 
the eigendecomposition involves complex numbers instead of straightforward real numbers.

In machine learning, however, we are typically working with real symmetric matrices, 
which can be conveniently and efficiently decomposed into real-only eigenvectors and real-only eigenvalues. 
If A is a real symmetric matrix then...

A = Q Λ Q^T

...where Q is analogous to V from the previous equation 
except that it's special because it's an orthogonal matrix.
'''

S = np.array([[2, 1], [1, 2]])  # real symmetric matrix

Evl, Evc = np.linalg.eig(S)\

Evl_diag = np.diag(Evl)

# Let's confirm A = Q Λ Q^T

S_eig_decom = np.dot(Evc, (np.dot(Evl_diag, Evc.T)))

print(S_eig_decom) # which equals to S

# Note: We can demonstrate that S is an orthogonal matrix cause (S^T)S = S(S^T) = I

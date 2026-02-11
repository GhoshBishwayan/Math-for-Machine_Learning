'''
Reln. between Determinants and Eigenvalues

det(X) = product of all Eigenvalues of X 
'''

import numpy as np
import matplotlib.pyplot as plt
from plot_utils import plot_vectors

X = np.array([[1,2,4],[2,-1,3],[0,5,1]])


X_det = np.linalg.det(X)

lambdas, V =  np.linalg.eig(X)

X_eigen_product = np.prod(lambdas)

# print("Determinants: ", X_det)
# print("Eigenvalues Product: ", X_det)

'''
|det(X)| in Numpy - it quantifies volume change as a result of applying X

if |det(X)| = 0
    X collapses space completely in at leat one dimension, thereby eliminating all volume
if 0 < |det(X)| < 1
    X contracts volume to some extent
if |det(X)| = 1
    X preserves volume exactly
if |det(X)| > 1
    X expands volume
'''

X_det_abs = np.abs(X_det) 
# means applying the Matrix X to tensor the volume will change based on X_det_abs

'''
Lets see with variuos |det(x)| on a basis vector
'''

B = np.array([[1,0],[0,1]])

plot_vectors([B[0], B[1]], ['lightblue', 'lightgreen'])
plt.xlim(-1, 3)
plt.ylim(-1, 3)
plt.show()
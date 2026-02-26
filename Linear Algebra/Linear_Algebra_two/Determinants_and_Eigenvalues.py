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

'''
plot_vectors([B[0], B[1]], ['lightblue', 'lightgreen'])
plt.xlim(-1, 3)
plt.ylim(-1, 3)
plt.show()
'''

''' applying singular vector N to B, |det(X)|=0 '''

N = np.array([[-4., 1.],[-8.,2.]])

N_det = np.linalg.det(N)

NB = np.dot(N, B)

# print(NB)

N_eigval, N_eigvec = np.linalg.eig(N)

# print(N_eigval)
# print(N_eigvec)

''' This vector opposite of each other which means doesn't represent any volume '''
'''
plot_vectors([B[0], B[1], NB[:,0], NB[:,1]], ['lightblue', 'lightgreen', 'Blue', 'green'])
plt.xlim(-6, 3)
plt.ylim(-10, 4)
plt.show()
'''

''' applying Identity matrix I to B, |det(X)|=1 '''

I = np.array([[1,0],[0,1]])

I_det = np.linalg.det(I)

IB = np.dot(I, B)

# print(IB)
I_eigval, I_eigvec = np.linalg.eig(I)

# print(N_eigval)
# print(N_eigvec)


'''
plot_vectors([B[0], B[1], IB[:,0], IB[:,1]], ['lightblue', 'lightgreen', 'Blue', 'green'])
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.show()
'''

''' applying  |det(X)| = 1 , but change direction and shape but remain on there spans and volume'''

J = np.array([[-0.5, 0], [0, 2]])
J_det = np.linalg.det(J)
J_det_abs = np.abs(np.linalg.det(J))

JB = np.dot(J, B)

# print(JB)
J_eigval, J_eigvec = np.linalg.eig(J)

# print(J_eigval)
# print(J_eigvec)
'''
plot_vectors([JB[:,0], JB[:,1], B[0], B[1]], ['Blue', 'green', 'lightblue', 'lightgreen'])
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.show()
'''


'''let's apply the matrix D, which scales vectors by doubling along both the x and y axes'''

D = I*2

D_det =np.linalg.det(D)
DB = np.dot(D, B)

# print(DB)
D_eigval, D_eigvec = np.linalg.eig(D)

# print(D_eigval)
# print(D_eigvec)

plot_vectors([DB[:,0], DB[:,1], B[0], B[1]], ['Blue', 'green','lightblue', 'lightgreen'])
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.show()
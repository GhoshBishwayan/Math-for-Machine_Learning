'''
An eigenvector ('eigen' is German for "typical"; 
we could translate eigenvector to "characteristic vector") 
is a special vector v such that 
when it is transformed by some matrix (let's say A), 
the product Av has the exact same direction as v.

An eigenvalue is a scalar (traditionally represented as λ) 
that simply scales the eigenvector v such that the following equation is satisfied:

Av = λv


Eigenvectors and eigenvalues can be derived algebraically 
(e.g., with the "QR algorithm" (https://en.wikipedia.org/wiki/QR_algorithm), 
which was independently developed in the 1950s 
by both Vera Kublanovskaya and John Francis)
'''
import numpy as np
import matplotlib.pyplot as plt
from plot_utils import plot_vectors

A = np.array([[-1,4],[2,-2]])

lambdas, V = np.linalg.eig(A) # this will return Eigenvalue, Eigenvalue (lambdas, v) in this order as tuples

print("Eigenvector")
print(V) 

print("Eigenvalue")
print(lambdas)

# Now let's confirm  Av = λv  for the first Eigenvector

v = V[:,0] # first column of V which is the first eigenvector

lambdas_1 = lambdas[0] # first vector's eigenvalue

Av = np.dot(A, v) # Av

Lambda_v = np.dot(lambdas_1, v) # λv

'''
plot_vectors([Av, v], ['blue', 'lightblue'])  # The vector didn't change its course and only extended
plt.xlim(-1, 2)
plt.ylim(-1, 2)
'''

v2 = V[:,1] # second column of V which is the second eigenvector 

lambdas_2 = lambdas[1] # second vector's eigenvalue

Av2 = np.dot(A, v2)

Lambda_v2 = np.dot(lambdas_2, v2) 

"""
plot_vectors([Av2, v2], ['green', 'lightgreen'])
plt.xlim(-2, 4)
plt.ylim(-4, 2)

"""

plot_vectors([Av2, v2, Av, v], ['green', 'lightgreen', 'blue', 'lightblue'])
plt.xlim(-2, 4)
plt.ylim(-4, 2)

plt.show()
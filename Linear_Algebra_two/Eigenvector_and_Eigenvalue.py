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

A = np.array([[-1,4],[2,-2]])

lambdas, V = np.linalg.eig(A) # this will return Eigenvalue, Eigenvalue (lambdas, v) in this order as tuples

print("Eigenvector")
print(V) 

print("Eigenvalue")
print(lambdas)
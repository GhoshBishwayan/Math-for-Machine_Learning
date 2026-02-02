import numpy as np

X = np.array([[4, 2], [-5, -3]])

# Matrix Inversion
Xinv = np.linalg.inv(X)

print("Matrix Inversion using Numpy ",Xinv)

print("X.X^-1 = Identity Matrix of length n (using Numpy) ", np.dot(X, Xinv))


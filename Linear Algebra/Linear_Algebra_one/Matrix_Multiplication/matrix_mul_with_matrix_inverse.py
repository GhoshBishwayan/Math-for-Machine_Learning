import numpy as np
import torch


X = np.array([[4, 2], [-5, -3]])

# Matrix Inversion
Xinv = np.linalg.inv(X)

print("Matrix Inversion using Numpy ",Xinv)

print("X.X^-1 = Identity Matrix of length n (using Numpy) ", np.dot(X, Xinv))


# using pytorch

X_pt = torch.tensor([[4. , 2.], [-5., -3.]])

Xinv_pt = torch.inverse(X_pt)

print("Matrix Inversion using PyTorch ",Xinv_pt)
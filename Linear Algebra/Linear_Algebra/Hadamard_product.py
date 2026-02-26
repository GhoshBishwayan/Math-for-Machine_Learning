import torch
import numpy as np

# Scalar operations

X = np.array([[25, 2], [5, 26], [3, 7]])
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])

print("Python operators: ",(X+2)*3)

print("PyTorch functions: ",torch.mul(torch.add(X_pt, 2), 3))

# Handamand Product /  element-wise product

A = X+2

print("'A' Tensor ", A)
print("'A' and 'X' Addition ", A+X)
print("'A' and 'X' Multiplication ", A*X)
print("'A' and 'X' Subtraction ", A*X)



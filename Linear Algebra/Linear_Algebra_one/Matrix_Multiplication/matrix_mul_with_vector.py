import numpy as np
import torch

A = np.array([[3, 4], [5, 6], [7, 8]])

b = np.array([1, 2])

print("Numpy Matrix Multiplication with Vector: ",np.dot(A, b)) # even though technically dot products are between vectors only

A_pt = torch.tensor([[3, 4], [5, 6], [7, 8]])

b_pt = torch.tensor([1, 2])

torch.matmul("PyTorch Matrix Multiplication with Vector: ", A_pt, b_pt) # like np.dot(), automatically infers dims in order to perform dot product, matvec, or matrix multiplication
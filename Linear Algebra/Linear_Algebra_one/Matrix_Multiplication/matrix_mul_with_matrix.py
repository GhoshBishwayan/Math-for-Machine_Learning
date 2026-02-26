import numpy as np
import torch

A = np.array([[3, 4], [5, 6], [7, 8]])

B = np.array([[1, 9],[2, 0]])

print("Matrix Multiplication(Two Matrices) using Numpy: ",  np.dot(A,B))


#converting numpy array to pytorch tensor
A_pt = torch.from_numpy(A)

B_pt = torch.tensor([[1,2],[9,0]]).T

print("Matrix Multiplication(Two Matrices) using PyTorch: ",  torch.matmul(A_pt, B_pt))
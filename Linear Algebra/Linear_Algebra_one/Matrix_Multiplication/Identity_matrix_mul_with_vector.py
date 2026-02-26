import torch

I = torch.tensor([[1,0,0],[0,1,0],[0,0,1]])  #Identity Matrix

x_pt = torch.tensor([25,10,2]) #Vector

print(torch.matmul(I, x_pt))

''' Multiplying Identity Matrix with a Vector will be that Vector '''
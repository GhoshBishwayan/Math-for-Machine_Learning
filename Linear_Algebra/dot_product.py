import numpy as np
import torch

x = np.array([25,2,5])
y = np.array([0,1,2])

print("Implementing dot using Numpy ",np.dot(x,y))

x_pt = torch.tensor([25,2,5])
y_pt = torch.tensor([0,1,2])


# print("Implementing dot using Numpy, passing PyTorch Vector",np.dot(x_pt,y_pt))
# We can pass integer based pytorch tensors to numpy to performs dot product But it is slow best if we avoid it
# Since Numpy will convert Pytorch tensors to Numpy array 

print("Implementing dot using PyTorch, passing decimal/float based Vectors ", torch.dot(torch.tensor([25.,2.,5.]),torch.tensor([0.,1.,2.])))

# Integer based vector won't work with torch.dot so we pass float based vector

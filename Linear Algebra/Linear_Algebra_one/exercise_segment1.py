import torch

x = torch.tensor([[42, 4, 7, 99],[-93, -3, 17, 22]])

#1. Whats the position of 17?
print(x[1,2])
'''Similar to L2 Norm which was for Vectors Frobenius Norm is for Matrices '''
import numpy as np
import torch

x = ([1,2],[3,4])

# Manually
f_n = (1**2 + 2**2 + 3**2 + 4**2)**(1/2)

# Using a built in function
f_n_inbuilt_fnc = np.linalg.norm(x)

print("Frobenius Norm using NP in built fnc ", f_n_inbuilt_fnc)

# PyTorch

x_pt = ([1.,2.],[3.,4.]) # float type tensors req for torch.norm

x_pt_norm = torch.norm(x)

print("Frobenius Norm using PyTorch ", x_pt_norm)
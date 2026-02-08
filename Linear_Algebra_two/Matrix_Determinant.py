import numpy as np

X = np.array([[4, 2], [-5, -3]])

print(np.linalg.det(X))

# Now an example of a matrix with determinant 0 which can't be invertible

N = np.array([[-4, 1],[-8, 2]])

detN = np.linalg.det(N) # 0.0

'''LinAlgError("Singular matrix")'''
# Ninv = np.linalg.inv(N) # This will give singular matrix error



'''Using PyTorch'''

import torch

X_pt = torch.tensor([[4, 2], [-5, -3.]]) #must be float type

detX_pt = torch.det(X_pt)

print(detX_pt)
import torch
import numpy as np

# Scalar operations

X = np.array([[25, 2], [5, 26], [3, 7]])
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])


X.sum()
torch.sum(X_pt) # sum of all the row + all the col

# Specific axis 

X.sum(axis=0)
X.sum(axis=1)

print(torch.sum(X_pt, 0)) # sum of col1, sum of col2...
print(torch.sum(X_pt, 1)) # sum of row1, sum of row2...

''' 
Many other operations can be applied with reduction along all or a selection of axes
    - maximum
    - minimum
    - mean 
    - product
used less then summation that we did above
'''
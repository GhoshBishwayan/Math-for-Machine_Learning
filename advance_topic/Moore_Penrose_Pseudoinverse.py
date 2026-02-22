'''
Even if a matrix can't be inverted, solving equation may still be possible by other means 
Such 'other mean' 

Moore-Pensore Pseudoinverse


A^+ = V(D^+)U.T
 
where, U,D,V are SVD of A
D^+ =  (D with reciprocal of all-non zero elements)^T

'''
import numpy as np
import torch

A = np.array([[-1,2],[3,-2],[5,7]])

# svd
U, d, VT = np.linalg.svd(A)

# V
V = VT.T

# UT

UT = U.T

# To get D^T first need to do 
D = np.diag(d)

# then we would take the transpose of the resulting matrix
# Because D is a diagonal matrix, this can be done in a single step by nverting D:
Dinv = np.linalg.inv(D)

# D^+ must have the same dimensions as A^T in order for V(D^+)U.T matrix multiplication to be possible
Dplus = np.concatenate((Dinv, np.array([[0,0]]).T), axis=1)

# A^+

Aplus = np.dot(V, np.dot(Dplus, UT))

print("Moore-Penrose Pseudoinverse : ")
print(Aplus)

# Using Numpy .pinv()

Aplus_np = np.linalg.pinv(A)

print("Moore-Penrose Pseudoinverse (Numpy in-bult) : ")
print(Aplus_np)



# Pytorch-version

A_pt = torch.tensor([[-1,2],[3,-2],[5,7.]])

U_pt, d_pt, VT_pt = torch.linalg.svd(A_pt)

# A^+ = V(D^+)U.T

# D^+

D_pt = torch.diag(d_pt)
Dinv_pt = torch.linalg.inv(D_pt)

# Matching dimensions 
zero_col = torch.zeros(Dinv_pt.shape[0], 1)   # (2 × 1)
Dplus_pt = torch.concatenate((Dinv_pt, zero_col), dim=1)



Aplus_pt = VT_pt.T @ Dplus_pt @ U_pt.T
A_pt_plus = torch.pinverse(A_pt)

print("Moore-Penrose Pseudoinverse (Pytorch) : ")
print(A_pt_plus)

print("Moore-Penrose Pseudoinverse (Pytorch-manually) : ")
print(Aplus_pt)

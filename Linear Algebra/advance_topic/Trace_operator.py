'''
Denoted as Tr(A)
Simply the sum of the diagonal elements of a matrix.
'''

import numpy as np

A = np.array([[25,2], [5,4]])

Tr_A = np.trace(A)

# print(Tr_A)

'''
The trace operator has a number of useful properties that come in handy while rearranging linear algebra equations, e.g:

Tr(A) = Tr(A^T)
Assuming the matrix shapes line up: 
Tr(ABC) = Tr(CAB) = Tr(BCA) // A,B,C matrices

the trace operator can provide a convenient way
to calculate a matrix's Frobenius Norm:

||A|| = Tr(AA^T)^1/2
'''

import torch

Ap = torch.tensor([[25,2.], [5,4.]])

Ap_T = Ap.T

Ap_fr = torch.linalg.matrix_norm(Ap, ord='fro')

print(Ap_fr)

AP_FR = torch.sqrt(torch.trace(torch.matmul(Ap,Ap_T)))

print(AP_FR)
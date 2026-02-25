'''
Denoted as Tr(A)
Simply the sum of the diagonal elements of a matrix.
'''

import numpy as np

A = np.array([[25,2], [5,4]])

Tr_A = np.trace(A)

print(Tr_A)
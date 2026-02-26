'''
While plotting gets trickier in higher-dimensional spaces, 
we can nevertheless find and use eigenvectors with more than two dimensions. 

Here's a 3D example (there are three dimensions handled over three rows):
'''

import numpy as np
import matplotlib.pyplot as plt
from plot_utils import plot_vectors_3d

X = np.array([[25, 2, 9], [5, 26, -5], [3, 7, -1]])

lambdas_X, V_X = np.linalg.eig(X)

print(V_X) # 3 columns 3 Eigenvectors 
print(lambdas_X, end="\n") # 3 Eigenvalues for each Eigenvectos
 

# Xv = λv

Xv1 = np.dot(X, V_X[:,0])
Lambda_v1 = np.dot(lambdas_X[0], V_X[:,0])
print('first Xv ',Xv1, end="\n")
print('first λv ',Lambda_v1, end="\n")

Xv2 = np.dot(X, V_X[:,1])
Lambda_v2 = np.dot(lambdas_X[1], V_X[:,1])
print('second Xv ',Xv2, end="\n")
print('second λv ',Lambda_v2, end="\n")

Xv3 = np.dot(X, V_X[:,2])
Lambda_v3 = np.dot(lambdas_X[2], V_X[:,2])
print('third Xv ',Xv3, end="\n")
print('third λv ',Lambda_v3, end="\n")

'''
Wip
fig, ax = plot_vectors_3d([Xv1, V_X[:,0], Xv2, V_X[:, 1], Xv3, V_X[:,2]] ,
             ['green', 'lightgreen', 'blue', 'lightblue', 'brown', 'pink'])

ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_zlim(-30, 30)

plt.show()
'''
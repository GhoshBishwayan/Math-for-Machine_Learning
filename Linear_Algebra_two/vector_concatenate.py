import numpy as np

v1 = np.array([3,1])
v2 = np.array([-3,6])
v3 = np.array([-1,7])

V = np.concatenate((np.matrix(v1).T,
                    np.matrix(v2).T,
                    np.matrix(v3).T),
                   axis = 1
                   )

print("Vector concatenated to create Matrix using Numpy: ")
print(V)
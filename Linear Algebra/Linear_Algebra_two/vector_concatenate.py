import numpy as np
import matplotlib.pyplot as plt
from Matrix_properties import plot_vectors

v1 = np.array([3,1])
v2 = np.array([-3,1])
v3 = np.array([-1,2])
v4 = np.array([3,-1])

V = np.concatenate((np.matrix(v1).T,
                    np.matrix(v2).T,
                    np.matrix(v3).T,
                    np.matrix(v4).T),
                   axis = 1
                   )

print("Vector concatenated to create Matrix using Numpy: ")
print(V)

# funtion to convert column of matrix to 1D vector:
def vectorfy(mtrx, clmn):
    return np.array(mtrx[:,clmn]).reshape(-1)

ve =  vectorfy(V,0)

print(ve) # which is basically v1
print(ve == v1)

A = np.array([[-1,4],[2,-2]])
AV = np.dot(A,V)

plot_vectors([vectorfy(V, 0), vectorfy(V, 1), vectorfy(V, 2), vectorfy(V, 3),
             vectorfy(AV, 0), vectorfy(AV, 1), vectorfy(AV, 2), vectorfy(AV, 3)],
            ['lightblue', 'lightgreen', 'lightgray', 'orange',
             'blue', 'green', 'gray', 'red'])
plt.xlim(-12, 12)
plt.ylim(-12, 12)

plt.show()
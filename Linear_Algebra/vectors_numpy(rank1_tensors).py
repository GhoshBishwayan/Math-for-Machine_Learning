import numpy as np

x = np.array([25, 2, 5])

print("Vector: ", x)
print("Length of the Vector: ", len(x))
print("Length of the Vector: ", x.shape)
print("Length of the Vector(using Numpy): ",type(x))
print("First element of Vector: ",x[0])
print("Type of each element: ", type(x[0]))

# Vector Transposition

y = np.array([[25, 2, 5]])
y_t = y.T

print("Vector before transpose: ", y)
print("Shape of the Vector before transpose: ", y)

print("Length of the Transpose Vector: ", y_t.shape)
print("The Transpose Vector: ", y_t)
import torch

x_pt_pt = torch.tensor([25, 2, 5])

print("Vector: ", x_pt_pt)
print("Length of the Vector: ", len(x_pt_pt))
print("Length of the Vector: ", x_pt_pt.shape)
print("Length of the Vector(using Numpy_pt): ",type(x_pt_pt))
print("First element of Vector: ",x_pt_pt[0])
print("Ty_ptpe of each element: ", type(x_pt_pt[0]))

# Vector Transposition

y_pt = torch.tensor([25, 2, 5])
y_pt_t = y_pt.T

print("Vector before transpose: ", y_pt)
print("Shape of the Vector before transpose: ", y_pt)

print("Length of the Transpose Vector: ", y_pt_t.shape)
print("The Transpose Vector: ", y_pt_t)
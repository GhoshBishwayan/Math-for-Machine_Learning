import torch  # pip install pytorch

# print(torch.__version__)

x_pt = torch.tensor(25) # type specification optional, e.g.: dtype=torch.float16


print(x_pt)
print(x_pt.shape)

### Scalars in PyTorch

# * PyTorch and TensorFlow are the two most popular *automatic differentiation* libraries (a focus of the [*Calculus I*](https://github.com/jonkrohn/ML-foundations/blob/master/notebooks/3-calculus-i.ipynb) and [*Calculus II*](https://github.com/jonkrohn/ML-foundations/blob/master/notebooks/4-calculus-ii.ipynb) subjects in the *ML Foundations* series) in Python, itself the most popular programming language in ML.
# * PyTorch tensors are designed to be pythonic, i.e., to feel and behave like NumPy arrays.
# * The advantage of PyTorch tensors relative to NumPy arrays is that they easily be used for operations on GPU (see [here](https://pytorch.org/tutorials/beginner/examples_tensor/two_layer_net_tensor.html) for example).
# * Documentation on PyTorch tensors, including available data types, is [here](https://pytorch.org/docs/stable/tensors.html).
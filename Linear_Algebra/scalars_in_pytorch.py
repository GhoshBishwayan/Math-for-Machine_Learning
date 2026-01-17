import torch  # pip install pytorch

# print(torch.__version__)

x_pt = torch.tensor(25) # type specification optional, e.g.: dtype=torch.float16


print(x_pt)
print(x_pt.shape)


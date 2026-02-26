import torch

import matplotlib.pyplot as plt
from plot_utils import plot_vectors

# Av = λv
A_p = torch.tensor([[-1, 4], [2, -2.]]) # must be float type

# eigens = torch.eig(A_p, eigenvectors=True)
lambdas_cplx, V_cplx = torch.linalg.eig(A_p)

# print(lambdas_cplx)
# print(V_cplx)

V_p = V_cplx.float()
lambdas_p = lambdas_cplx.float()

v_p = V_p[:,0]
lambda_p = lambdas_p[0]
# print(v_p)

Av_p = torch.matmul(A_p, v_p) # Av

Lambda_vp = lambda_p * v_p  # λv

# Now for the second vector
v2_p = V_p[:,1]

lambda2_p = lambdas_p[1]

Av2_p = torch.matmul(A_p.float(), v2_p.float())

Lambda_v2p = lambda2_p.float() * v2_p.float()

# print(Av2_p)
# print(Lambda_v2p)

plot_vectors([Av_p, v_p, Av2_p, v2_p], 
             ['green', 'lightgreen', 'blue', 'lightblue'])

plt.xlim(-1,4)
plt.ylim(-3,2)

plt.show()
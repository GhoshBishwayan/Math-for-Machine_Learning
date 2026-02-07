import numpy as np
import matplotlib.pyplot as plt
from plot_utils import plot_vectors

v = np.array([3, 1])

'''
plot_vectors([v], ['lightblue']) # before is with light color
plt.xlim(-1, 5)
plt.ylim(-1, 5)  # Note: write  _= plt.ylim(-1,5) for jupyter notebook
'''

# 2nd commit
I = np.array([[1,0],[0,1]]) # 2*2 Identity Matrix

v_after = np.dot(v,I) # Matrix Multiplication with Identity Matrices
'''
plot_vectors([v_after], ['blue']) # after is darker color
plt.xlim(-1,5)
plt.ylim(-1,5)
'''

# 3rd commit - Flips vector to x-axis
E = np.array([[1,0],[0,-1]])

Ev = np.dot(E, v)
'''
plot_vectors([v, Ev], ['lightgreen', 'green'])
plt.xlim(-1,5)
plt.ylim(-3,3)
'''

# 4th commit - Flips vector to y-axis 
Y = np.array([[-1,0],[0,1]])
Yv= np.dot(Y, v)
'''
plot_vectors([v, Yv], ['lightgreen', 'green'])
plt.xlim(-4,4)
plt.ylim(-1,4)
'''

# 5th commit - with matrix
M = np.array([[-1,4],[2,-2]])
Mv = np.dot(M, v)

v2 = np.array([2,1])

plot_vectors([v, np.dot(M, v2)], ['lightgreen', 'green'])
plot_vectors([v, Mv], ['lightgreen', 'green'])
plt.xlim(-1,6)
plt.ylim(-1,6)

# Commented out because I am using the function on another programms

plt.show()


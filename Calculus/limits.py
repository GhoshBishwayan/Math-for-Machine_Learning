'''
limit (x^2-1/x-1)
(x->1) 

y= x^2 -1/x-1
y= (x+1)(x-1)/x-1
y = x+1

the function is undefined at x = 1
so there will be a open hole at (1,2)
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 5, 100)
y = x+1

mask = x != 1
x = x[mask]
y = y[mask]


fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.axvline(x=1, color='purple', linestyle='--')
plt.axhline(y=2, color='purple', linestyle='--')
ax.plot(x,y)
ax.scatter(1, 2, facecolors='white', edgecolors='blue', s=100)

plt.show()
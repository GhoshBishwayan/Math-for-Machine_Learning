'''
2x - 3y = 15 ...1
4x + 10y = 14 ...2

we need to isolate y from both equation
1. y = -(15-2*x) / 3
2. y = (14 - 4x) / 10

Solve this linear operation
(x,y) = (6, -1)
'''



import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,1000)
y1 = -(15-2*x) / 3 #eqn-1
y2 = (14 - 4*x) / 10 #eqn-2

fig, ax = plt.subplots()
fig.canvas.manager.set_window_title("Elimination_eqn_visualizing")

plt.xlabel('x')
plt.ylabel('y')

ax.set_xlim([0,9])
ax.set_ylim([-5,8])

ax.plot(x, y1,label='eqn-1' ,c='green')
ax.plot(x, y2,label='eqn-2' ,c='blue')

plt.axvline(x=6, color='red', linestyle='--')
_ = plt.axhline(y=-1, color='red', linestyle='--')

ax.legend()
plt.show()
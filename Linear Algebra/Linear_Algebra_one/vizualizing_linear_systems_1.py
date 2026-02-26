'''
y=3x ....1
-5x+2y=2 .....2

we need to isolate y from both equation
1. y= 3*x
2. y= 1 + (5*x)/2

Solve this linear operation
(x,y) = (6,-1)
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,1000)
y1 = 3*x #eqn-1
y2 = 1 + (5*x)/2 #eqn-2

fig, ax = plt.subplots()
fig.canvas.manager.set_window_title("Substitution_eqn_visualizing")

plt.xlabel('x')
plt.ylabel('y')

ax.set_xlim([0,3])
ax.set_ylim([0,8])

ax.plot(x, y1,label='eqn-1' ,c='green')
ax.plot(x, y2,label='eqn-2' ,c='blue')

plt.axvline(x=2, color='red', linestyle='--')
_ = plt.axhline(y=6, color='red', linestyle='--')

ax.legend()
plt.show()
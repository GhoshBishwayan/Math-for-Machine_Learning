import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = x**2 + 2*x + 2

fig, ax = plt.subplots(2, 2, figsize=(10, 8))  # 2x2 grid

# Plot 1 - Wide view
ax[0, 0].plot(x, y)
ax[0, 0].set_title("Wide View(original)")

''' 
There are no straight lines on the curve. 
If we zoom in infinitely close, however, we observe curves that approach lines. 
This enables us to find a slope m(tangent) anywhere on the curve, including to identify where m=0: 
'''

# Plot 2 - Zoom 1
ax[0, 1].plot(x, y)
ax[0, 1].set_xlim([-2, 0])
ax[0, 1].set_ylim([0, 2])
ax[0, 1].set_title("Zoom Level 1")

# Plot 3 - Zoom 2
ax[1, 0].plot(x, y)
ax[1, 0].set_xlim([-1.5, -0.5])
ax[1, 0].set_ylim([0.5, 1.5])
ax[1, 0].set_title("Zoom Level 2")

# Plot 4 - Zoom 3
ax[1, 1].plot(x, y)
ax[1, 1].set_xlim([-1.01, -0.99])
ax[1, 1].set_ylim([0.99, 1.01])
ax[1, 1].set_title("Zoom Level 3")

plt.tight_layout()
plt.show()
'''
For regression problems, we typically have 
many more cases (n, or rows of X) than
features to predict (m, or columns of X)

Solve a  miniature example of such an overdetermined situation

We have eight data points (n=8)
'''

import matplotlib.pyplot as plt
import numpy as np


x1 = [0,1,2,3,4,5,6,7.] # E.g.: Dosage of drug for treating Alzheimer's disease
y = [1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37] # E.g.: Patient's "forgetfulness score"

title = 'Clinical Trial'
xlabel = 'Drug dosage (mL)'
ylabel = 'Forgetfulness'

fig, ax = plt.subplots()
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
ax.scatter(x1, y)
plt.show()

'''
Although it appears there is only one predictor (x1), 
our model requires a second one (let's call it x0) 
in order to allow for a y-intercept.

Without this second variable, 
the line we fit to the plot would need to pass through the origin (0, 0). 
The y-intercept is constant across all the points so we can set it equal to `1` across the board:
'''

x0 = np.ones(8)

X = np.concatenate((np.matrix(x0).T, np.matrix(x1).T), axis=1)

# print(X)

'''
we can calculate the weights w using eqn.:

w = (X^+)y
'''

w = np.dot(np.linalg.pinv(X), y)

print(w) # [[ 1.76       -0.46928571]]

# The first weight corresponds to the y-intercept of the line, which is typically denoted as b:

b = np.asarray(w).reshape(-1)[0]

# While the secong weight corresponds to the slope of the line, which is typically denoted as m:

m = np.asarray(w).reshape(-1)[1]

# With the weights we can plot the line to confirm it fits the points:

fig, ax = plt.subplots()

plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

ax.scatter(x1, y)

x_min, x_max = ax.get_xlim()
y_at_xmin = m*x_min + b
y_at_xmax = m*x_max + b

ax.set_xlim([x_min, x_max])
ax.plot([x_min, x_max], [y_at_xmin, y_at_xmax], c='C01')
plt.show()
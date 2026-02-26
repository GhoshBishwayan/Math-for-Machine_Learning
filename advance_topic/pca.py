'''
Principle Component Analysis
'''

from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()

print(iris.data.shape) #(no. of rows, no. of columns)

# features
print(iris.get("feature_names"))
print(iris.data[0:6,:])

from sklearn.decomposition import PCA

pca = PCA(n_components=2) # asking 2 components to plot in x-y graph

X = pca.fit_transform(iris.data)

print(X.shape) # should reduce no. of features which is column
print(X[0:6,:])

plt.scatter(X[:, 0], X[:, 1])


# Let's differentiate types of flowers here

print(iris.target.shape) # number of features
print(iris.target[0:6])

import numpy as np

unique_elements, counts_elements = np.unique(iris.target, return_counts=True)
np.asarray((unique_elements, counts_elements))

print(list(iris.target_names)) # different types of data's name

plt.scatter(X[:, 0], X[:, 1], c=iris.target)
plt.show()

'''
y= Xw
y is the outcome (house prices)
X is the features (1bhk, 2bhk etc.)
w is the vector unknows (Models learnable parameters)

Xw = y
(X^-1)Xw = (X^-1)y
Iw = (X^-1)y
w = (X^-1)y  [vector * Identity matrix = that vector]


Exercise:
4b + 2c = 4
-5b - 3c = -7

Here, 
    4,2,-5,-3 are the features
    4,-7 are house prices
    b & c are the weights of the features
    
w = (X^-1) y

X = [[4,2],[-5,-3]]
y = [4,-7]

w = [b,c]

'''     
import numpy as np

X = np.array([[4,2],[-5,-3]])

y = np.array([4,-7])

Xinv = np.linalg.inv(X)

# w = Xinv * y

w = np.dot(Xinv, y)
print(w)

'''
w = [b,c] = [-1,4]
b = -1
c = 4
'''
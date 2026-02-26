import numpy as np

x = np.array([25,2,5])

#manually
sum = 0
for i in x:
    sum = sum + i**2

l2_x_m = sum**(1/2)
print("Eucledian distance of x from origin", l2_x_m)

#using build-in funtion
print(np.linalg.norm(x))
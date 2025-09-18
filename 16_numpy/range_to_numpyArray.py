import numpy as np

a=np.arange(24)
print(a)

b=a.reshape(6,2,2)  # returns 6 vectors  -->> b is 3D matrix
#                   6 matrix of 2x2 
#      means reshape(a,b,c) = total a matrix of bxc 
print(b)
print(b.ndim)
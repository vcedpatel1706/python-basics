import numpy as np

x=np.array([[1,2,3],[4,5,6]])
z=np.array([[1,2,3],[4,5,6]])
y=np.array([[1,2],[4,5],[6,7]])

# matrix addition
print(x+z)
print(np.add(x,z))

# subtraction
print(x-z)
print(np.subtract(x,z))

# element wise multiplication
print(x*z)
print(np.multiply(x,z))

# matrix mul / dot ptoduct

print(x.dot(y))
print(np.dot(x,y))

# element wise division

print(x/z)
print(np.divide(x,z))

# 
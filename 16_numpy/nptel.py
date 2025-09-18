import numpy as np

arr=np.array([1,2,3,4,5,6],dtype=int)
print(arr)

print(type(arr))
print(len(arr))

print(arr.ndim)
print(arr.shape)

arr2=arr.reshape(2,3)
print(arr2)
print(arr2.shape)

arr3=arr.reshape(3,-1) # -1 means dimension calculated automatically
print(arr3.ndim)
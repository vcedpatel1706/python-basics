import numpy as np
list1=[1,2,3,4,5]
list2=[2,4,6,8,0]
list3=[1,3,5,7,9]

arr=np.array(list1)
print(arr)

arr2=np.array([list1,list2,list3])
print(arr2)
print(arr2.ndim) # 2D array em

print(arr2.size)
print(arr2.itemsize)
print(arr2.transpose)

arr3=arr2.reshape(1,15)
print(arr3)
arr3.shape=(5,3)
print(arr3)
import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(np.sum(a))
print(np.sum(a,axis=0)) # axis=0 means col. wise
print(np.sum(a,axis=1)) # axis=1 means all operation performs row wise


# wrong 

# print(np.multiply(a))
# print(np.multiply(a,axis=0)) 
# print(np.multiply(a,axis=1))
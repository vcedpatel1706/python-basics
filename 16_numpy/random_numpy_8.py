import numpy as np

# float bw 0 and 1

x=np.random.rand()
print(x)
arr=np.random.rand(2,3)
print(arr)

# random ints

y=np.random.randint(1,10)
print(y)

z=np.random.randint(1,11,size=3)
print(z)

brr=np.random.randint(1,12,size=(2,3))
print(brr)

# normal dist (mean=0, std=1)

w=np.random.randn(5)
print(w)
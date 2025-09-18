# Write a program using Numpy to count number of “C”
# element wise in a given array

import numpy as np

words=np.array(['cable','cd','ccc','pockct','ved'])

count_c=np.char.count(words,'c')
print("count of c i each word = ",count_c)
# *** different mathods to copy LIST ***


fruits=['apple','banana','mango','grapes','lichi']

# m-1
# fruits2=fruits // same refrence is given in this method only

# m-2
# fruits2=['apple','banana','mango','grapes','lichi']

# m-3
# fruits2=fruits[:]

# m-4
# import copy
# fruits2=copy.copy(fruits)
# fruits2=copy.deepcopy(fruits)

fruits2=fruits.copy()

print(fruits2==fruits)
print(fruits2 is fruits)
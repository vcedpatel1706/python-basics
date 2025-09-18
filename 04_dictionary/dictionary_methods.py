numbers={1:'ved',2:'nisarg',3:'vaibhav',4:'nirmit',5:'goti'}
digits={4:'vansh',3:'man'}
print(len(numbers))
print(numbers)

# access values
# 1
print(numbers[2])
# 2
print(numbers.get(2))
# print(number.get(8))  -->> error if not exist

# update values
# 1
numbers[5]='hc'
print(numbers)
# 2  (have to give dictionary in .update method)
numbers.update({2:'pv'}) # or..
numbers.update(digits)
print(numbers)


# pop methods(return deleted elements)
print(numbers.pop(2))  # have to provide key

print(numbers.popitem()) # no need to provide index, remove last 

del numbers[4] #-->> to delet element completly from memory

print(numbers)

# key update
numbers[22]=numbers.pop(3)
print(numbers)

# insert new element
numbers[44]='saybo riksha wado'
print(numbers)


# retrive all keys or all values

print(numbers.keys())
print(numbers.values())

# clear and empty

numbers.clear()
print(numbers)

del numbers
# print(numbers)   --> gives error, bcz no such dict. exist
name=input('enter your name')
age=int(input('enter your name'))

# m-1(old method)
final='my name is {}.i am {} years old'
print(final.format(name,age))

# m-2
print(f'my name is {name}. i am {age} tears old.')

# normal method 
print('my name is',name,' i am of ',age)

# so what is need of formatting
#   cleaner syntax
#   control on space(normal leaves space)
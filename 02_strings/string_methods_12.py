# in vscode by clicking three times we can select the current      line and b clicking 4 time we can select whole code


name='patel ved maheshbhai'
name.upper() # if we dont print it it do nothing
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())


print(name.islower())
# likewise .isupper,.islower,.......


# btw all these methods dont changes the original string.

print(name.isalnum())
# likewise .isnumeric,.isalpha....

print(name.count("e"))
print(name.replace('ved','vidhi'))

print(name)


print(name.find('a'))
print(name.index('a'))  # work of both is same but if no such char/str exist then find return -1 and index gives error.
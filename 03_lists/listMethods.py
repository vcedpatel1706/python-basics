# *** wkt list is mutable so unkike string, all changes will done
#     in list ***

# append
l=[10,11,12]
l2=[55,33]
l.append(77)
l.append(l2)
print(l)

# extend
l=[10,11,12]
l2=[55,33]
# l.extend(14)  -- error
l.extend(l2)
print(l)

# reverse

l.reverse()  # it reverse string but return null
print(l)

# sort(sort element of list in ascending)

l.sort()
print(l)

# pop (returns the deleted value)
print(l.pop())
print('after normal pop',l)

print(l.pop(2))
print('after deleting indexed pop',l)

# remove
l.remove(11) #removed the specified element ,returns null
print(l)

# claear  -->> make empty the list

l.clear()
print(l)

# del -->> deletes the complet list

del l
# print(l)  -->> gives error bcz no list l exist
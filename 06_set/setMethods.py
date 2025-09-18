s={10,20,30,10,30,40,50}
s1=set()

# 1
print(s)

# add element
s.add(33)
print(s)


# pop  (removes any random element),(reeturns deleted value)
#      ( is set is empty give error)
print(s.pop())
print(s)
# s1.pop()


# remove (deletes given value),(if element not found give error)
#        (returns null)
s.remove(10)
print(s)


# discard   (deletes given value) , (if not found don't give error,#                                    do nothing)
#           (return null)
s.discard(33)
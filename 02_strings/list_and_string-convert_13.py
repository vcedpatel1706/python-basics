# list -->> string
    # but we can't convert hetrogeneous list

l=['ved',17,11.6,1+2j,True]
l1=['ved','patel','vidhi']
str="".join(l1)
str1=" ".join(l1)


print(str)
print(str1)
print("_".join(l1))


# string to list

hobby="dancing, singing, reading, cleaning, talking"
print(hobby.split())
     # by default it split by space if no space in string then whole string will treated as one element

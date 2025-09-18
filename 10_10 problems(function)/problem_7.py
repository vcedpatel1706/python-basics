def sumNum(*args):
    # for experiment:
    print(args)
    # print(*args)
    print(type(args))
    return sum(args)

print(sumNum(1,2))
print(sumNum(1,2,3,4))
print(sumNum(1,4,3,5,7,8,6,))

#  by experiment we know that args will give tuple(iterable)

# we can do so..(without inbuilt fxn sum(args))
# def sumNUm(args)
#   sum=0
#   for in in args:
#       sum+=i
#   return sum

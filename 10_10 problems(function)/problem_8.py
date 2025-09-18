# **kwargs ( keyword arguments)

# in *args -->> print(args was tuple) and which amount is variable means 1/2/3/44 ,any no. of i/p of value is allowed

# **kwargs -->> is same but for any no. of i/p of key-valur pair is allowed

def pairs(**kwargs):
    for ved,ptl in kwargs.items(): # it is not compulsary to write key,value here, it is good practice to do so
        print(ved,ptl)

pairs(name='ved',age=20,srname='patel')
pairs(age=22,abcd='ptk')
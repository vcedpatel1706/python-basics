#  it is example of closure (actual concept of closure) 

def chaicoder(num):
    def actual(x):
        return x**num
    
    return actual

result1=chaicoder(2)
result2=chaicoder(3)

# result1 and result2 have refrence of actual but both bring ot to different memory location
print(result1)
print(result2)

print(result1(4))
print(result2(4))
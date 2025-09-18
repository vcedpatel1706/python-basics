# wap to print factorial of number using while loop
number=int(input('enter the number'))
factorial=1

while number>0:
    factorial*=number
    number-=1

print(factorial)
 
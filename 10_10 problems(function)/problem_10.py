def factorial(number):
    if number<=1: return 1
    return number*factorial(number-1)

print (factorial(5))



# in recursion is not big thing to write recurisve but important thing is to how to exit(base case) the recyrsion(end/start/middle)
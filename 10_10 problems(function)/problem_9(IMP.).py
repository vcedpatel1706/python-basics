# it is very deep level concept(recomented to explore more)

# yiels is to return the value as well as remember the memory refrence of that.

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i


for num in even_generator(10):
    print(num)


# actually  what we are doing ?
#   we want that run even_generator      every time and return the value and remember the memory location of that, so for next time it don't start execution from start but starts from whereever execution was stopped.
#    to do so we can use yield
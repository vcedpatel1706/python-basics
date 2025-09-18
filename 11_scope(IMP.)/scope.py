username='ved'
name='vcmp'

def user():
    username='patel'
    print(username)
    print(name)  # if variable is not in scope of function, then go to nearest upper

print(username)
user()


# 2

x=17
def fun2(y):
    z=x+y
    return z

result=fun2(6)
print(result)

# 3(global keyword (advised that not use))

p=99
def fun3():
    global p
    p=11

print(p)
fun3()
print(p)

# 4
o=99
def f1():
    o=11
    def f2():
        print(o) # consider nearest upper
    f2()

f1()

# 4 *****( this concept is called closure)*******
print('4 started')

u=99
def f1():
    u=11
    def f2():
        print(u) # consider nearest upper
    return f2 # returning f2, don't calling



myResult=f1() # f1 returns f2, don't call f2

print(myResult) # ****new***** storing refrence of f2 at some memory location
myResult() # in above line my result have f2, now 
           # it is calling f2

#  we'll think that if we return only f2 so how it can identify value of u in f1, bcz it also return all the refrences associated with f2 ,actually it is called closure(/bag theory),return not only defination but also return all required variables and refrences

# before f1 returns f2 it don't print(u) within f2?
#       bcz, f2 don't called even, it only defined only and returned by f1.( see by def f2().... we define it dont called until someone called it.)


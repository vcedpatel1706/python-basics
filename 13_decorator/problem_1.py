# wap that count the timing that require to execute the function

import time # time has no relation with decorator

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()

        print(f'{func.__name__} ran in {end-start} time')

        return result
    return wrapper

@timer # aano meaning avo che k aana pachi nu function call karo 
def example_function(n):           # te pehla timer fxn call thy.
    time.sleep(n)

example_function(3)


# flow of working :
# it sees @ timer ,before python define example_function it must pass it to timer.
# python define wrapper inside timer and return wrapper-->> 
# when we call example function it means -->>
# example_function = timer(example_function)   ,, but timer return that point to wrapper, -->> when we call example_function it actually call wrapper and wrapper return result




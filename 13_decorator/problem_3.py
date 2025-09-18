import time

def cache(func):
    cache_memory={}
    print(cache_memory)
    def wrapper(*args,**kwargs):

        if args in cache_memory:
            return cache_memory[args]
        result=func(*args)
        cache_memory[args]=result

        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b


print(long_running_function(2,3))
# first function nu output avta 4 second lage che but, second time it is cache so it give output immediately.
print(long_running_function(2,3))



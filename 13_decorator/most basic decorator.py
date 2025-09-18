def debug(func):
    
    def wrapper():
        return func()
        
    return wrapper

def hello():
    print('hello)')
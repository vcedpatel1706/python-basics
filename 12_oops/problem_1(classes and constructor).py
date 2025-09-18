class Car:
    def __init__(self,brand,model): # constructor
        # it is like constructor in java
        self.brand=brand  
        # self is like this in java 
        self.model=model

    def engine(self):
        print('only V8 engine is allowed')

myCar=Car('land rover','velar')
print(myCar.brand)

myCar.engine()
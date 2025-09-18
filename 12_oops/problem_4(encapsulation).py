# Encapsulation : is concept oop that hiding the internal details of how object works and exposing only what is necessary.

class Car:
    def __init__(self,brand,model):
        # self.__brand=brand  we make variable privet by .__
        self.model=model
    
    def get_brand(self):# we make brand accessible by getter.
        # we can use any name instade of get_ but it is convention
        return self.__brand+'!'

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model) 
        
        self.battery_size=battery_size


myTesla=ElectricCar('tesla','model-5','4000')

print(myTesla.model)
print(myTesla.__brand)# we can't access attribute brand directly without method.******hence how we encapsulate attribute brand *****************

print(myTesla.get_brand())
        
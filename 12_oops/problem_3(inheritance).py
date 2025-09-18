# inheritance

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def carInfo(self):
        return f'{self.model} of {self.brand}'

class ElectricCar(Car): # ElectricCar inherits Car
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model) 
        # same as java
        # it is child class of car so it can also use __init() method of Car as well.
        self.battery_size=battery_size

myTesla=ElectricCar('tesla','model-5','4000')
print(myTesla.model)
print(myTesla.carInfo())

        
# proof that in inheritance object of child class is instance of both sub and superclass

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model) 
        self.battery_size=battery_size

myTesla=ElectricCar('tesla','model-5','4000')

print(isinstance(myTesla,ElectricCar))
print(isinstance(myTesla,Car))

# isinstance(object,class) is built-in function


        
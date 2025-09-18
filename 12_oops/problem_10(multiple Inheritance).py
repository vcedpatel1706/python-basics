class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Engine():
    def engine_info(self):
        return 'this is engine'

class Battery():
    def battery_info(self):
        return 'this is battery'

class ElectricCar(Car,Engine,Battery):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model) 
        self.battery_size=battery_size

myTesla=ElectricCar('tesla','model-5','4000')

print(myTesla.battery_info())
print(myTesla.engine_info())
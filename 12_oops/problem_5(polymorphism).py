class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def fuel_type(self):
        return 'petrol or disel'

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return 'electric charge'


tesla=ElectricCar('tesla','model s','4000kwa')
tata=Car('tata','safari')

print(tesla.fuel_type())
print(tata.fuel_type())


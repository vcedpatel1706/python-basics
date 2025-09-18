# to add functionality in previous problem:

class Car:
    def __init__(self,brand,model): # telephone line "self" is required
        self.brand=brand  
        self.model=model
    
    def carInfo(self):# telephone line "self" is required to use class variable within class
        return f'{self.model} of {self.brand}'

myCar=Car('land rover','velar')
print(myCar.brand)
print(myCar.model)

print(myCar.carInfo())
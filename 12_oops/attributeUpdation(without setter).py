# we can also update the attribute which are we gave before by constructor.

class Car:
    def __init__(self,brand,model): 
        self.brand=brand
        self.model=model

myCar=Car('land rover','velar')
print(myCar.brand)

myCar.model='maybach' # un restricted ( any one comes and put anything like 100/ ved etc..,,,, TO solve this use setter method)

print(myCar.model)
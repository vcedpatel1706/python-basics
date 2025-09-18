#  static method is the method that belong to class ,not to instance(jem class variable tem class methods)

# don't take 'self' as first parameter

#  can't access or modify the 

# static method can also called by object but it is not prefered way

class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.total_car+=1

    @staticmethod  # it is decorater,@staticmethod modifys the behaviour of method
    def car_description():
        return 'car is mean to transport'


my_car=Car('tata','safari')
print(my_car.car_description())
print(Car.car_description())

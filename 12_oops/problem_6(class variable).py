class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_car+=1  # or.. self.total_car+=1


Car('tata','safari')    
Car('mahindra','scorpio')
# yes ! you can make object like this , but use only this when you don't need object further

print(Car.total_car)



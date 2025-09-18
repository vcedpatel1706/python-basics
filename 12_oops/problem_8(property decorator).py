# property decoraror : make attribute read only = readable not writable(can't update)


# to make privvet attribute we have getter so what is need of
#  @property decorator,
# we need @property decorator for more cleaner way to access attribute , we don't need functin directly by attribute name

class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
    
    def get_brand(self):
        return self.__brand+'!'
    
    @property
    def model(self): # we can give any name of function.
        return self.__model
    
myCar=Car('tata','safari')

myCar.brand='maruti'
print(myCar.brand)

# myCar.model='harier'
# print(myCar.model)

# Q : though we made the brand and model privet, how it can be readable and writable directly without method.
# Ans :     bcz,these variable in last 4 line is different from__brand and model. 
#           by line-15 and line-18 we create new public vatiable of class (public variable = apde pehla thi class ma j normal variable banavia te = accessible from inside and outside from class.) 


# ***** now move back to actual problem *********

# we are using 'model' as @property decorator so now line-25,26 not work.

print(myCar.model)  # no need of model() to read bcz by @propery,, use only model 


# ********* @property and @property.setter is substitute of getter and setter
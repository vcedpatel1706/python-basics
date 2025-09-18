#  setter is use to put restriction on data entry.

class Student:
    def __init__(self, age):
        self.__age = age   # private variable

    def set_age(self, age):
        if age > 0:
            self.__age = age  # __ is for make atribute privet(no one can update without setter method)
        else:
            print("Age must be positive.")

    def get_age(self):
        return self.__age


s1 = Student(20)

print(s1.get_age())     # 🔓 20
s1.set_age(25)          # ✅ update with control
print(s1.get_age())     # 🔓 25
s1.set_age(-10)         # ❌ Invalid input

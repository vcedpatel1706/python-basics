# we can declate attribute by both inside and outside __init__
# 1) attribut outside __init__ is class variable .
# 2) attribute outside __init__ is instance variable

class Student:
    school = "Green Valley"  # class variable

    def __init__(self, name):
        self.name = name

s1 = Student("Amit")
s2 = Student("Neha")

print(s1.name)  # Amit
print(s2.name)  # Neha

print(s1.school)  # Green Valley
print(s2.school)  # Green Valley
# Now modify it only for s1
s1.school = "Red Valley"  # creates instance version
print(s1.school)  # Red Valley (instance-level)
print(s2.school)  # Green Valley (class-level still)

print(Student.school)



#  it is not compulsary to pass value in __init__.
# def __init__(self):
#    self.instance_var = 50

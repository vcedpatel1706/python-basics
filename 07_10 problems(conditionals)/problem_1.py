age=int(input("enter your age"))
if age<13:
    print('you are child')
elif age<20:  # don't write age>=13 and age <20 -->> it is foolishness.
    print('teenager')
elif age<60:
    print('adult')
else:
    print("senior")

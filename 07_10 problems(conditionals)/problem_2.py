age=int(input("enter your age"))
price=0

if age<18:
    isWednesday=bool(input("today is wednesday"))
    if isWednesday:
       print('6')
    else:
        print('8')
else:
    isWednesday=bool(input("today is wednesday"))
    if isWednesday:
        print('10')
    else:
        print(12)
    

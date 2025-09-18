# for leap year : year is divisible by 4 but not by 100 or 
# divisible by 400

year=int(input('enter the year :'))

if ((year%4==0 and year%2!=0) or (year%400==0)):
    print("it is leap year")
else:
    print('not a leap year')


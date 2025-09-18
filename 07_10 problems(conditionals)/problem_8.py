passward=input('enter your passward')

len=len(passward)
if len<6:
    strength='weak'
elif len<=10:
    strength='strong'
print('your passward is ',strength)

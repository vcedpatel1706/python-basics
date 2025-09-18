# wap to find first non repeted character
name='peerptor'


for i in name:
    if (name.count(i)==1):
        firstNonRepeted=i
        break

print('first non repeted character is ',firstNonRepeted)


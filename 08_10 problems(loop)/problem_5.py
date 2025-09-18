#  wap to find firat non repeted character

name='peerptor'

for i in name:
    if (i not in name[name.index(i)+1:]):
        firstNonRepeted=i
        break

print('first non repeted character is ',firstNonRepeted)



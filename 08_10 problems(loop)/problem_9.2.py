l=['apple','mango','grapse','pineaple','chiku','chiku','pineaple']

for i in l:
    if(i in l[l.index(i)+1:]):
        print(i)
        break
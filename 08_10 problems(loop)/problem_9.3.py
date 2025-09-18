l=['apple','mango','grapse','pineaple','chiku','chiku','pineaple']

uniqueitem=set()
for i in l:
    if i in uniqueitem:
        print('duplicate is ',i)

    uniqueitem.add(i)

print(uniqueitem)
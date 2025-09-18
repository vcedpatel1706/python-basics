# wap to find duplicate element in list. if duplicate found then return duplicate element and exit break.


#  we are making code for firat duplicate finder

l=['apple','mango','grapse','pineaple','chiku','chiku','pineaple']


for i in l:
    if(l.count(i)!=1):
        print(i)
        break
        

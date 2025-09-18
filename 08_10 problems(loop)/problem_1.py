list1=[1,-2,3,-4,0,5,6,-4,7,-8,9]
positiveCount=negativeCount=0
for i in list1:
    if i<0:
        negativeCount+=1
    else:
        positiveCount+=1  

print('negative count is ',negativeCount, 'and positive count is ',positiveCount)  



     
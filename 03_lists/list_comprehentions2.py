# wap to differentiate the odd and even numbers

numbers=[22,43,89,6,34,37,9,7,17]
oddNums=[]
evenNums=[]

# m-1 : using loop and condition
# m-2 : using list comprehentions

evenNums=[x for x in numbers if x%2==0]
oddNums=[x for x in numbers if x%2!=0]

print(oddNums,evenNums)
teaTypes=('Green','Black','masala')
(a,b,c)=teaTypes # or.....   a,b,c=teaTypes
print(a,b,c)
(ved,patel,vidhi)=teaTypes  # think why we don't used ' ' .


ranking=(1,2,3,4,5,6)

a,b,*c=ranking
print(a)
print(b)
print(c)

a,*b,c=ranking
print(a,b,c)




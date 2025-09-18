numbers=[1,2,3,4,5,6]

squares={x:x**2 for x in numbers}

print(squares)

# copy of dict

copySquares=squares.copy()  #w.k.t it created different refrence
print(copySquares)
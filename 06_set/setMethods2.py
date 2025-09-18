s1={1,2,3}
s2={1,3,4}
s3={2,1,3}


# union,intersection,difference,symmetric_difference RETURNS result

# union
s4=s1.union(s2)  # or..  s4=s1|s2
print(s4)
# intersection
s5=s2.intersection(s3)  # or.. s5=s2&s3
print(s5)
# difference
s6=s4.difference(s5) # or.. s6=s4-s5
print(s6)
# symmertic difference( yog - ched /or/ no comman element)
s7=s4.symmetric_difference(s2) # or.. s7=s4^s2
print(s7)



# now,, update/intersection_update/difference_update/symmetric_difference_update  will do operation and RETURNS null

# s1.update(s2) : union of s1 and s2 will store in s1
# s1.difference_update(s2)  : result stored in s1
# s1.intersection_update(s2) : result stored in s1
# s1.symmetric_difference_update(s1) : result stored in s1


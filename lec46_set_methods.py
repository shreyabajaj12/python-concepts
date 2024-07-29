s1={1,2,5,6}
s2={3,6,7}
# print(s1.union(s2))
# print(s1,s2)
# s1.update(s2)
# print(s1)
# s2.intersection_update(s1)
# print(s2)
# d=s1.symmetric_difference(s2)
# print(d)
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
s1.add(34)
# s1.remove(21)  #gives error when value not present
s1.discard(21)     #does not throw error

item=s1.pop()   #we don't know which value is going to get popped out
print(item)
print(s1)
del(s1)
# clear(s2)

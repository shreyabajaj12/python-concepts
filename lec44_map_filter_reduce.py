# map
def cube(x):
    return x**3
print(cube(3))

l=[1,2,4,5,6]
# newl=[]
# for item in l:
#     newl.append(cube(item))
newl=list(map(cube,l))
print(newl)


# filter
def filter_fun(a):
    return a>4
newnewl =list(filter(filter_fun,l))
print(newnewl)

#   Reduce
from functools import reduce
sum=reduce(lambda x,y:x*y,l)
print(sum)
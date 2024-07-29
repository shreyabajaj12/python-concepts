b ={}
print(type(b)) # this syntax will create empty dic not set
a ={2,3,5,7,2} # collection of non repetative elements
print(type(a))
print(a)
c= set()
print(type(c)) #use to print empty set
c.add(4)
c.add(76)
c.add(45)
c.add((2,3,4,5,6))  #we can add tuple but not the list & dict becoz list is not hashable i.e, content can change elements i.e, list and dictionary
print(len(c))    # prints the length
print (c)
a.remove(2)
print(a)





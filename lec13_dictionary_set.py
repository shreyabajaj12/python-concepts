myDic = {
    "Fast" : "in a quick manner",
    "Shreya" : "winner",
    "Marks" : [1,2,3],
     "anotherdict":{'harry':'player'},   # nested dictionary
     1:2
}
print(myDic['Fast'])
print(myDic['Shreya'])

print(myDic['anotherdict']['harry'])
myDic['Marks'] =[34,23,22]
print(myDic['Marks'])      #these are mutable


print(list(myDic.keys()))  #prints the keys of that dic
print(myDic.values())      
print(myDic.items())     #print the keys and values for all key value pair for iteration

#print(myDic)
updateDict = {
    "Raj" : "Birthday"
}
myDic.update(updateDict)   #update the dict by adding them
print(myDic)
print(myDic.get('Shreya1'))    # returns none whereas without get method returns error when not present
myDic=dict(hyderabad=23,mumbai=34)
print(myDic)

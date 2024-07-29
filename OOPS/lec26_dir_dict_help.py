x=[1,23,34]
print(dir(x))

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1
    
p=person("Shreya",19)
print(p.__dict__)

print(help(str))
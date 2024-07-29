class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id=id
class Programmer(Employee):
    def __init__(self,name,id,lang):
        # self.name=name
        # self.id=id
        super().__init__(name,id)
        self.lang=lang

rohan=Employee("Rohan Das",123)
mohan=Programmer("mohan",234,"java")
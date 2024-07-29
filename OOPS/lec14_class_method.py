class Employee:
    company ="Camel"
    salary=100
    location="Delhi"

    # def changeSalary(self,sal):
    #     self.salary= sal    #this does not changes the class attribute it just creates the new instance of salary na dassigh the value to it
    def changeSalary(self,sal):
        self.__class__.salary = sal   #this helps to change the class attribute
        #alternative
    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal

e = Employee()
print(e.salary)
e.changeSalary(344)
print(Employee.salary)

class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company} ")

    @classmethod     # used to change the class mathod rather than the instance.
    def changeCompany(cls,newCompany):
        cls.company=newCompany

e1 =Employee()
e1.name ="Harry"
# e1.company="Microsoft"
e1.show()
e2 =Employee()
e2.name="Shreya"
e2.changeCompany("Tesla")
e2.show()
print(Employee.company)
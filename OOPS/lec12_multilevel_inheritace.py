class Person:
    def __init__(self):
        print("Initializing Person...\n")
    country="India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"
    def __init__(self):
        super().__init__()
        print("Initializing Employee")
    def getsalary(self):
        print(f"Salary is {self.salary} ")
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am taking breath..")

class Programmer(Employee):
    company ="Fiverr"

    def getSalary(self):
        print(f"No salary to programmer")
    def takeBreath(self):
         super().takeBreath()
         print("I am a programmer so I am taking breath++...")

p =Person()
p.takeBreath()
print(p.country)
e = Employee()
e.takeBreath()
print(e.country)
print(e.company)
pr =Programmer()
pr.takeBreath()
print(pr.company)


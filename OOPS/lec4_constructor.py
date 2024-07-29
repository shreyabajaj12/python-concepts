class Employee:
    company ="Google"

    def __init__(self,name,salary,subunit):   #constructor
        self.name = name
        self.salary =salary
        self.subunit = subunit
        print("Employee is created")
    def getdetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self,signature):
        print(f"Salary for this one working in {self.company} is {self.salary} {signature}")
    @staticmethod
    def greet():
        print("Good Morning Sir")

harry = Employee("Harry",100,"You Tube")
harry.getdetails()

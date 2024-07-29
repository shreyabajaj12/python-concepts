class Employee:
    company ="Google"
    def getSalary(self,signature):
        print(f"Salary for this one working in {self.company} is {self.salary} {signature}")
    @staticmethod
    def greet():
        print("Good Morning Sir")
harry=Employee()
harry.salary=100000
harry.getSalary("thanks")  
#  Employee.getSalary(harry)
   #inside it , it gets converted to this hence we are giving a parameter so we req self for it


harry.greet()  #Employee.greet()


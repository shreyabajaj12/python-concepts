class Employee:
    company ="Google"

    def showDetails(self):
        print(f"This is an employee of {Employee.company}")

class Programmer():
    language ="python"
    def getLanguage(self):
        print(f"The language is {self.language}")
    def showDetails(self):
        print(f"This is an employee of {self.language}")

class Genius(Employee,Programmer):
    types="javafx"
    def java(self):
        print(f"the language is{self.types}")


e =Employee()
e.showDetails()
p=Programmer()
p.showDetails()
l=Genius()
l.java()
l.showDetails()
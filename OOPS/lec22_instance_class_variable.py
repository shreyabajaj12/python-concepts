class Employee:
    noOfEmployee=0
    companyName="Apple"   #class variable
    def __init__(self,name):
        self.name=name
        Employee.noOfEmployee +=1
    def showDetails(self):
        print(f"The name of the Employee is{self.name} and works in {self.companyName} in a {self.noOfEmployee}")
    
emp1=Employee("shrey")
emp1.companyName="Amazon"      #instance variable
emp1.showDetails()
emp2=Employee("Raj")
emp2.showDetails()
Employee.showDetails(emp1)   # the upper one gets converted to to this hence we are giving a parameter as emp1 so we have to pass self
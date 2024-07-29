class Employee:
    company ="Google"       #    it is common for all the members under the class  .. class attribue
harry =Employee()
shrey =Employee()
shrey.company="Amazon"       #    we can change by taking the name of the object
shrey.salary=400              #   instance variable/ attribute
harry.salary=300              # instance attribute takes preferance over class attribute during assignment and retrival
print(harry.company)
print(shrey.company)
print(harry.salary)

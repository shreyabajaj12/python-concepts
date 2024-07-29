# class Employee:
#     company="Bharat Gas"
#     salary=4500
#     salarybonus =500

#     @property            #getter method
#     def totalSalary(self):
#         return self.salary + self.salarybonus
#     @totalSalary.setter
#     def totalSalary(self,val):
#         self.salarybonus = val - self.salary
# e = Employee()
# print(e.totalSalary)
# e.totalSalary=5800
# print(e.salary)
# print(e.salarybonus)




# class myclass:
#     def __init__(self,value):
#         self._value=value
#     def show(self):
#         print(f"Value is {self._value}")

#     @property
#     def ten_value(self):
#         return 10*self._value

#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value=new_value/10

# obj =myclass(10)
# obj.ten_value=67
# print(obj.ten_value)
        

class Name:
    def __init__(self,nam):
        self.nam=nam
    def shrey(self):
        print(f"the name is {self.nam}")
    @property
    def newname(self):
        return self.nam+"rose"
    @newname.setter
    def newname(self,concatinate):
        self.nam=concatinate

latest=Name("shreya")
latest.newname="shrebajaj"
print(latest.newname)    
latest.shrey()

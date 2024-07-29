# class Complex:
#     def __init__(self,r,i) :
#         self.real = r
#         self.imaginary =i
#     # def __add__(self,c):
#     #     return Complex(self.real+c.real,self.imaginary+c.imaginary)
#     def __mul__(self,c):
#         mulreal = (self.real*c.real-self.imaginary*c.real)
#         mulimaginary =(self.real*c.imaginary - self.imaginary*c.real)
#         return Complex(mulreal,mulimaginary)
#     def __str__(self):
#         return f"{self.real}+{self.imaginary}i"
# c1 = Complex(1,4)
# c2 = Complex(8,5)
# print(c1*c2)

class student:
    __group="ece"
    __report="fail"

    def __init__(self,group,age):
        self.__group=group
        self.__report=report
    def getdetails(self):
        print(self.name,self.age,self.__group,self.__report)
name=input("name:")
age=int(input("age:"))
group=input("group:")
report=input("pass/fail")
s1=student(name,age)
print("Student Report Card")
s1.setdetails(group,report)
s1.getdetails()
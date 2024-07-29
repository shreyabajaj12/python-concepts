# a=True
# print(a:=False)

# numbers=[1,2,3,4,5]
# while(n:=len(numbers)) >0:
#     print(numbers.pop())

# happy=True
# print(happy)
# print(happy:=True)

foods=list()
while True:
    food=input("What food do you like?: ")
    if food=="quit":
        break
    foods.append(food)
print(foods)

food=list()
while (food :=input("What food do you like?:")) !="quit":
    foods.append(food)





# class student:
#     def __init__(self,name,id,mathsmaarks,scimarks):
#         self.name=name
#         self.id=id
#         self.mathsmaarks=mathsmaarks
#         self.scimarks=scimarks
#     def one(self):
#         print(self.name)
#         print(self.id)
#     def two(self):
#         print(self.mathsmaarks)
#         print(self.scimarks)
# stu1=student("rohan",34,12,34)
# stu2=student("raj",45,67,78)
# stu1.one()
# stu2.two()

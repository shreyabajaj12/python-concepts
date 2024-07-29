# def percent(marks1):  #this is a function
#     return (sum(marks1)/400)*100   #space left at 1st ia called indent
# marks = [23,78,98,87]
# percentage1 =percent(marks)
# print(percentage1)

# def greet(name = "Stranger"):  #the stranger word will act as a default argument
#     print("good day," + name)

# def mysum(num1,num2):
#     return num1 + num2


# greet("raj")
# greet() #when nothing is passed 
# w =mysum(233,333)
# print(w)
# def helloworld():
#     print("helloworld\ngood morning\nhave a nice day")
# helloworld()



# def add(x,y):
#     a=x+y
#     print(a)
# def sub(x,y):
#     b=x-y
#     print(b)
# def mul(x,y):
#     c=x*y
#     print(c)
# d=int(input("x:"))
# e=int(input("y:"))
# add(d,e)
# sub(d,e)
# mul(d,e)
# def add(x,y):
#     return(x+y,(x+y)/2)
# def sub(x,y):
#     return(x-y)
# x=int(input("x:"))
# y=int(input("y:"))
# print("sum:",add(x,y))
# print("sum:",sub(x,y))


#PARAMETERS AND ARGUMENTS
# def add(a,b):
#     return a+b
# a=int(input("a:"))
# b=int(input("b:"))
# print(add(a,b))

# def sayhello(username):
#     greet="hello"
#     print(greet+" "+username)
# users=['ram','neha','ashutosh','shreya']
# sayhello(users[0])
# sayhello(users[1])
# sayhello(users[2])
# sayhello(users[3])

# def simplecalc(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
# simplecalc(a=3,b=5)       in case of keyword argument write the assgning factor
# simplecalc(b=4,a=5)
# simplecalc(6,5)

# def saysomething(name,message):
#     print("Good"+message+" "+name)
# nam=input("name: ")
# msg=input('morning/night: ')
# saysomething(name=nam,message=msg)
# saysomething(nam,msg)

# def nam(*,name,age):
#     print(name,age)
# x=input("name: ")
# y=int(input("age:"))
# nam(name=x,age=y)
# nam(age=y,name=x)
# nam("harry","18")

# def simplecalc(a,b=100):
#     print(a+b)
#     print(a-b)
#     print(a*b)
# num1=int(input("a: "))
# num2=int(input("b: "))
# simplecalc(num1)
# simplecalc(num1,num2)

# def fun1(*,name="panda",age=16):
#     print(name, 'is',age ,'years old')
# name1='Arana'
# name2='karuna'
# age1='12'
# fun1(name=name1)
# fun1(name=name2)
# fun1()
# fun1(name=name2,age=age1)
# fun1(age=age1)
'''
def mysum(*args):
    r=0
    for i in args:
        r=r+i
    return r
print (mysum(1,4,7,8,9,3,5))
print(mysum(4,5))

tax=lambda salary:salary*20/100
salary=int(input("salary:"))
print("Tax to be paid is:",tax(salary))

doublenum:lambda a:a*2
a=int(input("a:"))
print(doublenum(a))

def square(x):
    return x**2
list1=[1,2,3,4,5]
print(list(map))

def test1():
    a=50
    b=80
    print(a,b)
def test2():'''

# global variable
a=int(input("a:"))
def changeglobal():
    global a
    a=200
def changelocal():
    a=500
    print("local value:",a)
    print("global a before function",a)
print("global a before function:",a)
changeglobal()
changelocal()
print("global a after function call:",a)

# function composition
def square(x):
    r=x**2
    return r
def double(x):
    r=x*2
    return r
x=int(input("num:"))

# print(square(double(x))


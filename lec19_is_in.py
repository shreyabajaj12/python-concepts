# a = None
# if (a is None):
#     print("yes")
# else:
#     print("no")

a =[45,56,6]
print(435 in a)
num1 = int(input("enter no 1"))
num2 = int(input("enter no 2"))
num3 = int(input("enter no 3"))
num4 = int(input("enter no 4"))

if(num1>num4):
    f1 = num1
else:
    f1 =num4

if(num2>num3):
    f2 = num2
else:
    f2 =num3

    if(f1>f2):
        print(str(f1) +"is greatest")
    else:
        print(str(f2) +"is greatest")
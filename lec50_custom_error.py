# a=int(input("Enter any value between 5 and 9"))
# if(a<5 or a>9):
#     raise ValueError("The value should be between 5 and 9")

a=input("Enter any value between 5 and 9")
try:
    if(int(a)<5 or int(a)>9):
        raise ValueError("The value should be between 5 and 9")
except:
    if a==str(a) and a!="quit":
        raise ValueError("Value should be between 5 and 9")
finally:
    print("code run successfully")
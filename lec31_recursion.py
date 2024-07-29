# def factorial_recursive(n):
#     if n ==1 or n==0:
#         return 1
#     return n*factorial_recursive(n-1)

# f= factorial_recursive(5)
# print(f)


# def max(num1 ,num2 ,num3):
#     if(num1 >num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3
        
# m = max(3,5,1)
# print("the value of the max is"+ str(m))
 

def sum(n):
    if n==0:
        return 0
    return sum(n-1)+n

c =2
print(sum(2))
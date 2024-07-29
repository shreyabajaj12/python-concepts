import random
# def check(comp,user):
#     if comp==user:
#         return 0
#     if(comp==0 and user==1):
#         return -1
#     if(comp==1 and user==2):
#         return -1
#     if(comp==2 and user==0):
#         return -1
#     return 1
# comp=random.randint(0,2)
# user=int(input("0 for snake,1 for water,and 2 for gun"))

# score=check(comp,user)
# if(score==0):
#     print("is a draw")
# elif (score==-1):
#     print("you lose")
# else:
#     print("you won")
def check(comp,user):
    count=0
    if comp==user:
        return count
    if(comp==1 and user==0):
        count+=1
        return count
    if(comp==2 and user==1):
        count+=1
        return count
    if(comp==0 and user==2):
        count+=1
        return count
    
while  True:

    comp=random.randint(0,2)
    user=int(input("0 for snake,1 for water,and 2 for gun"))
    if user == -1:
        break  
    score=check(comp,user)
    print(score)

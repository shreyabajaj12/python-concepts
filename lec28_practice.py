# num = int(input("enter the number"))
# for i in range(1,11):
#     print(str(num) + "X" +str(i)+"="+str(i*num))    #alternate method
#     print(f"{num}X{i}={num*i}")


l1 = ["Harry" , "Sohan" , "Shreya" , "Raj"]
for name in l1:
    if name.startswith("S"):
        print("Hello " + name)                     


num = int(input("enter the number: "))
prime = True
for i in range(2,num):
    if(num%i ==0):
        prime = False
        break
if prime:
    print("this number is prime")
else:
    print("this number is not prime")


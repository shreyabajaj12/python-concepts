import time
# def usingWhie():
#     i=0
#     while i<50000:
#         i=i+1
#         print(i)
    
# def usingfor():
#     for i in range(50000):
#         print(i)
# init=time.time()
# usingfor()
# t1=(time.time()-init)
# init=time.time()
# usingWhie()
# print(time.time()-init)
# print(t1)

print(4)
time.sleep(3)
print("print this after 3 seconds")

t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)
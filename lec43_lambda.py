# def double(x):
#     return x*2
# def cube(x):
#     return x**3

def appl(fx ,value):
    return 6+ fx(value)
# double=lambda x:x*2  #takes x and returns x*2
# avg=lambda x,y:(x+y)/2
# print(double(5))
# print(avg(1,2))
print(appl(lambda x:x**3 ,2))
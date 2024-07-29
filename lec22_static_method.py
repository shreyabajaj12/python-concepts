class Math:   #  it is not always required to put self as a inside a method we can use @staticmethod
    def __init__(self,num):
        self.num=num
    def sumofno(self,n):
        self.num +=n

    @staticmethod 
    def add(a,b):    #does not required to put self
        return a+b

a=Math(4)
print(a.add(2,3))
print(Math.add(12,34))  #both can be used
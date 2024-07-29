class Sample:
    a="Harry"

obj =Sample()
obj.a ="Vickey"
print(Sample.a)  # it dosen't change the class attribute it just makes the instance attribute set
print(obj.a)
#-------------------------------------------------------------------------------------------
@staticmethod
def greet():
    print("Hello welcome to the best best calculator of the world")
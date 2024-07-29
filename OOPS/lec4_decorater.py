def greet(fx):
    def mfx(*args,**kwargs):  # it takes the value in it
        print("Good morning")
        fx(*args,**kwargs)
        print("Thanks for using")
    return mfx

@greet
def hello():
    print("Hello world")
def add(a,b):
    print(a+b)

hello()
# greet(hello)()     it can be assumed and pass through like this when @greet is not passed
greet(add)(1,2)
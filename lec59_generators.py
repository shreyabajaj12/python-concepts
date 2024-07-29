def my_generator():
    for i in range(5000):
        yield i       # returns a generator and suspends the execution of the function until next keyword is asked for

gen =my_generator()
# print(next(gen))
# print(next(gen))         it return the value on fly and it doesnot not stores any value anywhere hence it does not uses any memory space
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)

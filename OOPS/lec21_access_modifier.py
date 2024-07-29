class Employee:
    def __init__(self):
        self.__name="Harry"
a=Employee()
# print(a.__name)   cannot be accesed directly it is private
print(a._Employee__name)
#canbe accessed directly

print(a.__dir__())
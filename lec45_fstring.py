letter="Hey my name is {1} and I am from {0}"
country ="India"
name="Shreya"

print(letter.format(country,name))
print(f"Hey my name is{name} and i am from {country}")
price=69.09999
txt=f"For only {price:.2f} dollars!"
# print
print(txt)

# doc string
def square(n):
    '''Takes in a number n,returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)


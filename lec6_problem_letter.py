letter = '''Dear <|name|>,
A very 
Happy Birthday to you

Date : <|DATE|>
'''
print(letter)
name = input("enter ur name \n")
date = input("enter date\n")
letter =letter.replace("<|name|>" ,name)
letter =letter.replace("<|DATE|>" , date)
print(letter)




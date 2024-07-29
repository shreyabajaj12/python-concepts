# with open("log.txt")as f:
#     content = f.read()

# if 'python' in content.lower():
#     print("Yes python is present")
# else:
#     print("No python is not present")

content=True
i=1
with open("log.txt")as f:
    
    while content:
        content = f.readline()

if 'python' in content.lower():
    print(content)
    print("Yes python is present")
    print(i)
i+=1
# else:
#     print("No python is not present")
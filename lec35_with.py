with open("sample2.txt" ,"r") as f:
    a =f.read()
with open("sample2.txt","w") as f:
    a =f.write("me")
    print(a)
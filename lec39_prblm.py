words =["donkey","kaddu","mote"]
with open("Shrey.txt")as f:
    content = f.read()
for word in words:
    content = content.replace(word,"$^$#@$")


with open("Shrey.txt","w") as f:
    content = f.write(content)
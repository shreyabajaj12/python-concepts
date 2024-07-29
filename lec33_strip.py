def remove_and_split(string ,word):
    newStr =string.replace(word," ")
    return newStr.strip()  # strip fun helps us to remove unwanted spaces

this ="           how are you hey "
n =remove_and_split(this,"are")
print(n)
#print(this)
#print(this.strip())
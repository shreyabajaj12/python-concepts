f = open("sample.txt","r")
data = f.read()                    #used to just read 
print(data)
f.close()
# there are two modes in which we can dislpay
# text mode like .txt
# binary mode like .jpg
f = open("sample2.txt","w")
f.write("please write this file hey how are u dude ")  #used to write or make a new file
f.close()

f =open("sample2.txt","a")
f.write("i am appending")            #used to apend the existing file
f.write(" i am appending")            #used to apend the existing file
f.close()

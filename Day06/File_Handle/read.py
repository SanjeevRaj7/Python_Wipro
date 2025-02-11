'''''
f=open("test1.txt","r")
content = f.read()
#content = f.readlines()
print(content)
f.close()'''

#using with function its will close the file itself

with open("test1.txt","r") as f:
    data = f.read()
    print(data)
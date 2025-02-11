#2
#Implement a generator to yield all the lines from a large text file without loading the entire file into memory.
'''''
f=open("f.txt","w")
content = "hello"
f.write(content)
f.close()'''

def fun(name):
    with open(name,"r") as f:
        for i in f:
            yield i

name="f.txt"
for i in fun(name):
    print(i)



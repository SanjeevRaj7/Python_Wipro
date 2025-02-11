#stackframe
'''''
def f1():
    print("hi",end="")
    def f2(): # within the f1
        print("sanjeev")
    print("bye")

    return f2

ret = f1()
print(ret) # return the f2 address'''
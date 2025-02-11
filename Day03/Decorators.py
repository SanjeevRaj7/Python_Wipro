def func(f):
    return f
def disp():
    print("hello")

ret=func(disp)
print(ret,type(ret))

disp()
ret()# it will have the address of disp function

#using decorator
def func(f):
    print("hi ",end="") # Wrapper the text before calling the func
    f() # having the disp function address and call the value

def disp():
    print("sanjeev")

func(disp) # passing disp functon
print("*"*10)
#using wrapper
def func(f):
    def wrapper():
        print("hi ",end="") # Wrapper the text before calling the func
        f() # having the disp function address and call the value

    wrapper()

def disp():
    print("sanjeev")

func(disp)
print("*"*10)
#using @ symbol
def dFunc(f):
    def wrapper():
        print("Hi, ", end="") #wrapper
        f() #item
        print("Bye!") #wrapper

    return wrapper

@dFunc
def disp():
    print("Bhima")

'''
ret = dFunc(disp)

# print(ret, type(ret))
ret()

disp = dFunc(disp)
disp()
'''
disp()
print(disp)
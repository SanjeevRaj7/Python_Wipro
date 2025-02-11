#PRIME NUMBER USING FUNCTION
def isprime(num):
    flag = False
    if num < 2:
        return 0
    for i in range(2,(num//2)+1):
        if num % i == 0:
            flag = True
            break

    if flag :
        return 0
    else:
        return 1


print(isprime(10))

 #DOCSTRINGS
def func():
    "this is a function"
    pass

print(func.__doc__)#print the commands
print(dir())
print("__name__",__name__)#name of the file

# print(bin(2)[2:]) to clear value from binary

# Recursive
def func2(n):
    print(n)
    if n == 0:
        return 1
    return n * func2(n-1)

ret = func2(3)
print(ret)
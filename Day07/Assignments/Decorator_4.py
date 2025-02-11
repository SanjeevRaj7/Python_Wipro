#4
#Create a decorator that logs the input arguments and output of a function.




def log(func):
    def wrapper(*args,**kwargs):
        print(f'input {args},{kwargs}')
        r=func(*args,**kwargs)
        print(f'output {r}')
        return r
    return wrapper

@log
def add(a,b):
    return a+b
add(1,2)


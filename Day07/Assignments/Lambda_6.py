#6
#Write a lambda function to convert a list of strings to a list of integers, but raise an exception if conversion fails.

s=["5","6","2","8","9"]
try:
    x=list(map(lambda x : int(x),s))
    print(x)
except ValueError as e:
    print("value error",e)
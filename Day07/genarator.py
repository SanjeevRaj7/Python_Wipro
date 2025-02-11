def gen(n):
    for i in range(n):
        yield i**3

value = gen(10)
#print(next(value)) # print onle one value
#print(next(value))
for i in value:
    print(i)


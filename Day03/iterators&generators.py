nums=iter([1,2,3,4])
while True:
    try:
        print(next(nums))
    except StopIteration:
        break

#generators
def countdown(n):
    while n > 0:
        yield n
        n-=1
for num in countdown(10):
    print(num)

for num in countdown(20):
    print(num)

#generator expression
gExp=(i*i for i in range(5))
print(type(gExp))

while True:
    try:
        print(next(gExp))
    except StopIteration:
        break

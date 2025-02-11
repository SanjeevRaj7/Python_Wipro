#1
#Create a generator that yields prime numbers indefinitely.


def prime():
    x=2
    while True:
        for i in range(2,x):
            if x%i==0:
                break
        else:
            yield x
        x+=1

r=prime()
for i in r:
    print(i)



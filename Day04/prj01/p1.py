from functools import reduce


def func(x):
    return x*x
l1=[1,2,3]
l2=[4,5,6]
#m=map(func,l1,l2)
#print(list(m))

m=map(lambda x,y:x*y,l1,l2)
print(list(m))

r = reduce(lambda x,y:x*y,l1,10)
print(r)

val=[2,3,4]
f=filter(lambda x: "yes" if val[0]>1 else "no",val)
print(list(f))
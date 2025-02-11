#BUILT IN FUNCTIONS
#MAP
from functools import reduce


def fun(x):
    return x*x

l1=[1,2,3]
#tup=tuple(map(fun,l1)) # using map in single line
#print(tup)
m=map(fun,l1) #using map we are iterate the values in list
print(m)
t=tuple(m) # converting map to tuple to display values
print(t)

#using dictionary in MAP
d={'a':1,'b':2,'c':3}

d1=map(lambda x:(x[0],x[1]**2),d.items())
d1=dict(d1)
print(d1)

#REDUCE
def fun(v1,v2):
    return v1*v2
ret=1
num=[1,2,3,4,5]

for i in num :
    ret=fun(ret,i) # using loop

print(ret)
prd = reduce(fun,num) #using reduce function it reduce iterate object into single value
print(prd)


#FILTER
def f1(x):
    if x % 2 == 0:
        return True

l1 = [1,2,3,4,5]


l2 = []

for i in l1:
    if f1(i):
        l2.append(i)

print(l2)

flt = filter(f1,l1)
print(type(flt), list(flt))


def f2(x):
    if len(x) > 5:
        return True

words = ["apple", "banana", "kiwi", "blackberry"]
flt1 = filter(f2,words)
print(list(flt1))


#ZIP
L1=[1,2,3,4,5]
L2=[10,20,30]
czip = zip(L1,L2)
czip=list(czip)
print(czip)

m=[[1,2],[3,4],[5,6]]

transpose = zip(*m)
#print(list(transpose))
l3=list(map(list,transpose))
print(l3)


#ENUMERATE
names=['sanjeev','sanjay']
for index,element in enumerate(names,start=1): # we will start index with anything
    print(index,element) # gives the index of that element

#ANY/ALL
nums=[1,2,3,4,5]
print(all(x>0 for x in nums)) # if any one value is out of range it will false

nums=[1,2,3,4,5]
print(any(x<0 for x in nums))


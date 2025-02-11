from functools import reduce

l1=[1,2,3]

l=reduce(lambda x,y : x+ y,l1)
print(l)

l2=list(map(lambda x,l1))
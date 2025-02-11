#5
#Use a lambda function to find the intersection of two lists.

l1=[1,2,3,4,5]
l2=[2,3,6,7,8]

x=list(filter(lambda x: x in l2,l1))
print(x)

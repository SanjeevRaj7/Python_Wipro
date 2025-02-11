l1=[1,2,3,4]
print(l1,type(l1))
l1.append(5)
l1.insert(1,6)
l1.insert(len(l1)+10,7)
print(l1,type(l1))
l1.insert(-2,8)
print(l1,type(l1))
#l.clear() clear the list
#l.pop() remove last elemet and using index we can delete
#del l1 # delete the list
#print(l1) Nameerror

#sorted
l2=[5,4,3,2,1]
l3=sorted(l2)#not modify original values
print(l3)

#sort will affect the original list eg: l2.sort()
#count used to count the occurrence eg: print(l2.count(2))


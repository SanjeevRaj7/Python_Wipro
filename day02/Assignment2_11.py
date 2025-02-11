'''rotate array every kth element
i/p
No of Elememts in the list = 9
Enter the elements

1 2 3 4 5 6 7 8 9

i/p
k= 3

o/p
3 2 1 6 5 4 9 8 7 '''


n=int(input("enter a number of elements"))
l=list(map(int,input("enter a elements")))
print(l)
k=int(input("enter a value"))
r=[]
for i in range(0,n,k):
    r.extend(l[i:i+k][::-1])

print(r)
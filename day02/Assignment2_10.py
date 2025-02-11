'''Problem Statement:
Given an unsorted array a of size N of non-negative integers,
find a continuous sub-array which adds to a given number sum.

Input Format:
The first line contains an integer, denoting the size of the array.
The second line contains integers denoting the elements
of the array.
The last line contains an integer, denoting the sum. '''


n=int(input("Enter a number: "))
l=list(map(int,input(f"Enter {n} numbers: ").split()))
print(l)
s=int(input("enter a sum"))
print(f"Sum={s}")
for i in l:
    #print(i)
    for j in range(i+1,len(l)):
        if l[i]+l[j] == s:
            print(f"sum of index found at {i} and {j}")
else:
    print("no subarray found")


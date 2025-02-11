#ASSIGNMENTS
#1
'''Print series 0,3,8,15,24,35,48,63,80,99'''
n=[]
#for i in range(10):
 #   n.append(i**2+i+i)
#print(n)
x=[i**2+i+i for i in range(10)]
print(x)
#2
'''''
Write the logic to for incrementing Squared Number-Star Pattern.
Input Format      : Take N as input of type integer.
Output Format     : Print incrementing Squared Number-Star Pattern.

Constraints:
2<=N<=10
Sample Input:
5
Sample Output:
1*2*3*4*5
6*7*8*9*10
11*12*13*14*15
16*17*18*19*20
21*22*23*24*25 '''

n=1
for i in range(5):
    pattern=[]
    for j in range(5):
        pattern.append(str(n))
        n+=1
    print("*".join(pattern))

#3
'''Write a python program to print alphabet triangle.
Input: 5
Output:

     A
    ABA
   ABCBA
  ABCDCBA
 ABCDEDCBA '''

n=int(input("entre rows"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print(chr(65+j),end="")
    for j in range(i-2,-1,-1):
        print(chr(65+j),end="")
    print()


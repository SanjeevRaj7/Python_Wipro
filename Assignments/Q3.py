'''Problem Statement
You are given 3 strings A, B, and C. Your task is to find whether you can write both A and B using the characters of C. Not only that, after writing A and B from C, there should be no letter left in C.

Input Format
The first line contains A.
The second line contains B.
The third line contains C.'''
from xmlrpc.client import FastParser

a="ANNMMC"
b="LLDKKD"
c="ANNLLDKKCMMD"
flag=False
for i in a:
    if i in c:
        c=c.replace(i,"")
for i in b:
    if i in c:
        c=c.replace(i,"")
    if c=="":
        flag=True

if flag:
    print("YES")
else:
    print("NO")
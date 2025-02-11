'''Problem Statement
You are given a substring sss and main string ss Your task is to insert a substring at a given position p in the main string.

Input Format
The First line contains the main string ss.
The second line contains substring sss.
The third line contains integer position p at which the substring will be inserted.
Constraints'''

s=input("enter a string")
sub=input("enter a substring")
index=int(input("enter a position"))

for i in range(len(s)):
    if i==index:
        s=s[:i]+sub+s[i:]
print(s)
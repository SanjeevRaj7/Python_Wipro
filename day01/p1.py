#this is my program
print("hello")
a=10
print(id(a))#address
print(type(a))#datatype

s = str(102)
print(type(s),s)
print(s[0], s[1])
d = int(s[::-1])
print(d, type(d))

a=7
b=3

c = a/b
print(c,type(c))

d = a//b
print(d,type(d))

l1 = [1,2,3,4,5]

print(3 not in l1)

a=10
b=20
print(a>=b)
c=10
c **=10 #c = c+10
print(c)


a=10
b=20
c=3

print((a<=b) or (a<=c))
'''
AND
1 1 1
1 0 0
0 1 0
0 0 0


OR
1 1 1
1 0 1
0 1 1
0 0 0
'''

a=-1
print(not(a))

a=10
b=10
print(a is b)

a=5 # 0101
'''
1010 5 =>10
0011 3
====
0111
'''
print(a|3)

a = 5
print(~a)

a=5
'''
0101 << 1
1010 => 10

0101 >> 1
0010 => 2



a=1010 =>10
1010
0001 xor
====
1011 = 11
'''
print(a<<1)

print(a>>1)

print(10^1)
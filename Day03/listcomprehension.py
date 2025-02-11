List11=[i for i in range(1,11)]
print(List11)

#two
l1=[i for i in range(1,11)]+[i for i in range(11,21)]
print(l1)

#oddnumbers
l2=[i for i in range(1,21) if i%2!=0]
print(l2)

#odd&even
l3=[i for i in range(1,21) if i%2==0]+[i for i in range(1,21) if i%2!=0]
print(l3)

#print * in vowels
s=('sanjeev')
l8=[]
for i in s:
    if i in 'aeiou':
        l8.append("*")
    else:
        l8.append(i)

print(l8)
#
s='sanjeev'
l4=["*" if i in 'aeiou' else i for i in s]
l5=["".join("*") if i in 'aeiou' else i for i in s]
print(l4)
print(l5)

#without comprehension
l7=[]
for i in range(1,5):
    for j in range(6,9):
        l7.append(i*j)
print(l7)

#using comprehension
l6=[i*j for i in range(1,5) for j in range(6,9)]
print(l6)

#nested list
l9=[[1,2],[3,4],[5,6]]
l10=[]
for slist in l9:
    print(slist)
    for item in slist:
        print(item)
        l10.append(item)
print(l10)

#using
flist=[item for slist in l9 for item in slist]
print(flist)

#in function
def sq(x):
    return x*x

r=[sq(x) for x in range(1,5) if x%2==0]
print(r)

#dict
l11=[1,2,2,3,4]
print(dict.fromkeys(l11))#remove duplicate keys from the list using dictionary

ulist=[dict.fromkeys(x for x in l11)]
print(ulist)

#slice
l12=list(range(20))
slice=[x for x in l12[5:15:2]]
print(slice)

#reverse
l11=[1,2,2,3,4]
rlist=l11[::-1]
print(rlist)

rlist=[l11[i] for i in range(len(l11)-1,-1,-1)] #another method for reverse
print(rlist)
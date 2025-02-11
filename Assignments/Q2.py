ch=input("enter a word:")
ch1=sorted(ch) # it will covert to list and sorted
#print(ch1)
r=[]
flag=True

while ch1:
    if flag:
        for x in sorted(set(ch1)): # it will take only unique
            #print(ch1)
            r.append(x)
            ch1.remove(x)
    else:
        for x in sorted(set(ch1),reverse=True):
            r.append(x)
            ch1.remove(x)

#print(r)
print("".join(r))




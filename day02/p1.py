s1="hello"
s2='this is a python class \n "Bhima" sir is a tutor'
print(s2)

print("="*10)

start=1
end=start +1
step=1#skip the value
print(s1[start:end])
print(s1[start:end:step])

#reverse index
s3="hello world"
print(s3[:5:-1])

#TASK
s1="abcdef"
s2="1234567"
s3=""
i=0
while(i<len(s1)) or i<len(s2):
    if(i<len(s1)):
        s3+=s1[i]
    if(i<len(s2)):
        s3+=s2[i]
    i+=1
print(s3)

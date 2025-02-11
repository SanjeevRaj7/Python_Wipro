#LAMBDA
sqr = lambda x : x**2 # not create stackframes
print(sqr(5))
# using function also we create this but it will take stackframes

#using squares
nums=[1,2,3,4,5]
l=[(lambda x:x**2) (x) for x in nums]
print(l)

#odd/even
odd_even = lambda x : 'even' if x % 2 == 0 else 'odd'
print(odd_even(5))

#using list
l=[1,2,3,4,5]
l1=[(lambda x:'even' if x%2 == 0 else 'odd') (x) for x in l]
print(l1)

#using dictionary
d1 = {
'p1' :{
    'name': 'abc1',
    'age': 15
    },
'p2' :{
    'name': 'sanjeev',
    'age': 18
    },
'p3' :{
    'name': 'sanjay',
    'age': 25
    }
}

d3=list(filter(lambda x: x['age']>=18,d1.values()))
print(d3)

d4=[ v for k,v in d1.items() if v['age']>=18]
print(d4)

#mutiple statement

def add_and_mul(a,b):
    return (a+b,a*b)
op= lambda a,b: add_and_mul(a,b)
print(op(1,2))
'''Check whether a given number can be expressed as the sum of two prime number'''

from day02.Function import isprime

number=int(input("Enter a number: "))

if number > 1:
    prime=True
    for i in range(2,number):
        if number % i == 0:
           print(f"{number} is not a prime number.")
           break
        else:
            print(f"{number} is a prime number")
            break
else:
    print("enter a number greater than 1")
count =0
for i in range(2,number//2 +1):
    if isprime(i) and isprime(number - i):
        count += 1

ways = count
print(f"No of ways {ways}")




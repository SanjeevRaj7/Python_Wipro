#5
'''
Common Elements Across Collections (Sets & Tuples)
Problem Statement: Write a Python function that takes a list, a tuple, and a set as inputs
and finds the common elements between them. The function should return the result as a
sorted list.
Example Input:
list_input = [1, 2, 3, 4, 5]
tuple_input = (3, 4, 5, 6, 7)
set_input = {5, 6, 7, 8, 9}
Expected Output:
[5]
'''

list_input = [1, 2, 3, 4, 5]
tuple_input = (3, 4, 5, 6, 7)
set_input = {5, 6, 7, 8, 9}
new=[]
for i in list_input:
    if i in tuple_input and i in set_input:
            new.append(i)

print(new)
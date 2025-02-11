#2
'''
List to Nested Dictionary (Lists & Dictionaries)
Problem Statement: Write a function that takes a list of integers as input and converts it into
a nested dictionary. Each key in the dictionary should point to the next dictionary, and the
final key should point to None.
Example Input:
[1, 2, 3, 4]
Expected Output:
{1: {2: {3: {4: None}}}}
'''
def fun(list1):
    output = None
    print(type(output)) # class NoneType
    for i in list1:
        output ={i:output}
    return output

list1 = [1, 2, 3, 4]
result = fun(list1)
print(result)

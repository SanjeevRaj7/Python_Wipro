#6
'''Tuple Pair Sum Checker (Tuples & Lists)
Problem Statement: Write a function that takes a list of tuples, where each tuple contains
two integers. The function should return a list of tuples where the sum of the two integers is
greater than a given threshold.
Example Input:
input_tuples = [(1, 2), (3, 5), (0, 8), (2, 1)]
threshold = 6
Expected Output:
[(3, 5), (0, 8)]'''


input=([1,2],[3,5],[0,8],[2,1])
threshold = 6

output=[x for x in input if sum(x) > threshold]
print(output)
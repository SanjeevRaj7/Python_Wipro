#1
'''Unique Words and Their Count (Sets & Dictionaries)
Problem Statement: Write a Python program that takes a string of text as input and
performs the following:
1. Extract all unique words (case-insensitive) from the text using a set.
2. Count the occurrences of each word and store them in a dictionary.
3. Display the dictionary sorted by word frequency in descending order.
Example Input:
"Python is great. Python is simple. Simple is better than complex."
Expected Output:
{'is': 3, 'python': 2, 'simple': 2, 'great': 1, 'better': 1, 'than': 1, 'complex': 1}'''

text = "Python is great. Python is simple. Simple is better than complex."
s = text.lower().replace(".","").split()
print(s)
unique={}
for word in s:
    if word in unique:
        unique[word] += 1
    else:
        unique[word] = 1
sort = dict(sorted(unique.items(), key=lambda x: x[1], reverse=True))
print(sort)
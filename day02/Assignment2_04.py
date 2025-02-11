#4
'''Shopping List Organizer (Lists & Dictionaries)
Problem Statement: Write a function that organizes a shopping list. The input is a list of
tuples, where each tuple contains an item and its category (item, category). Group the
items by category into a dictionary where the keys are categories and the values are lists of
items.
Example Input:
[
('Apple', 'Fruits'),
('Carrot', 'Vegetables'),
('Banana', 'Fruits'),
('Broccoli', 'Vegetables'),
('Chicken', 'Meat')
]
Expected Output:
{
'Fruits': ['Apple', 'Banana'],
'Vegetables': ['Carrot', 'Broccoli'],
'Meat': ['Chicken']
}'''

items=[('Apple', 'Fruits'),('Carrot', 'Vegetables'),('Banana', 'Fruits'),
('Broccoli', 'Vegetables'),('Chicken', 'Meat')]

d=dict(items)
print(d)
d1={}
for x,y in d.items():
    print(d1)
    if y not in d1:
        d1[y]=[]
        d1[y].append(x)
    else:
        d1[y].append(x)

print(d1)



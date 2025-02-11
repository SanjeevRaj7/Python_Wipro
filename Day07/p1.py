import csv
'''content = [['name','age'],['sanjeev',21]]
with open("sample1.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerows(content)'''

with open("sample1.csv","r") as f:
    row1=csv.DictReader(f)
    for row in row1:
        print(row)
        print(row['name'],row['age'])

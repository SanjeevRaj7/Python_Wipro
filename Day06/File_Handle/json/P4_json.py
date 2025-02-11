#using json

import json

data={'_id':1,'name':'sanjeev','address':'coimbatore'}

#with open('p4data.json', 'w') as f: #to create json file
 #   json.dump(data,f)

with open('p4data.json', 'r') as f: # to read the json file and give the output
    d1=json.load(f)

print(d1)
'''''
#updating
d1['name'] = 'Sanjay'
with open('p4data.json', 'w') as f:
    json.dump(d1,f)

with open('p4data.json', 'r') as f:
    d1=json.load(f)

print(d1)  '''
#10
#Write a Python script to connect to a MongoDB database, insert multiple documents at once, and perform a complex query to find specific documents.

import pymongo
mycn =  pymongo.MongoClient("mongodb://localhost:27017/")
db=mycn["mydb"]
print(mycn.list_database_names())
#create table
mycol=db["eg"]
documents=[{'name':'sanjeev','age':21,'skills':['python']},
           {'name':'sanjay','age':21,'skills':['ui&ux']},
           {'name':'ajay','age':21,'skills':['java']},
           {'name':'Sagar','age':22,'skills':['python']}]

#mycol.drop() # TO DROP THE TABEL

x=mycol.insert_many(documents)

#to find
#print(x.inserted_ids)
query ={'skills':'python','age':22}
data=mycol.find(query)
print("__QUERYRESULT__")
for d in data:
    print(d)



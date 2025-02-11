#DELETING A DATA


import pymongo
mycn= pymongo.MongoClient("mongodb://localhost:27017/")
mydb = mycn["mydb"]

mycol = mydb["customers1"]
'''''
mylist = [ {'_id':1,'name':'abc1','address':'ad1'},
           {'_id':2,'name':'abc2','address':'ad2'},
           {'_id':3,'name':'abc3','address':'ad3'}]
x= mycol.insert_many(mylist)
print(x.inserted_ids)'''

data = mycol.find()

print(data) # it sotres the object of the collection.find()

data_all = mycol.find()

for d in data_all: # print all the data we created
    print(d)

#q={'address':'ad1'}
#mycol.delete_one(q)  # DELETING A ONE DATA to delete many mycol.delete_many()

# mycol.drop it will delete all the tables

#################################################
#UPDATING A VALUE
'''''
myquery = {'address':'ad2'}
newquery = {'$set':{'address':'Bangalore'}}
mycol.update_one(myquery,newquery) '''

################################################
# UPDATING A NAME USING A ADDRESS
'''''
myquery = {'address':{'$regex':'ad[0-9]'}}
newquery = {'$set':{'name':'Sanjeev'}}
mycol.update_one(myquery,newquery) '''

##################################################







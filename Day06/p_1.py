import pymongo

#print(pymongo.version) # show the version of pymongo

mycn = pymongo.MongoClient("mongodb://localhost:27017/") # connect my mongodb to this server
#mydatabase = mycn["mydb1"]  # create a database as mydb1

#print(mycn.list_database_names()) # connect local database and giving the available databases

if "mydb" in mycn.list_database_names(): # check the database is avilable
    print("database exists")


else:
    mydatabase = mycn["mydb"] # if not it create the database

mycollection = mydatabase["customers"] # creating a table customers

if "customers" in mydatabase.list_collection_names():
    print("collection exists")

#d1 = {'name':'Amit','address':'cbe'}
#x=mycollection.insert_one(d1)
#print(x.inserted_id)

# TO INSERT MANY VALUES
'''''
mylist = [ {'_id':1',name':'abc1','address':'ad1'},
           {'_id':2,name':'abc2','address':'ad2'},
           {'_id'':3,name':'abc3','address':'ad3'}]
x= mycollection.insert_many(mylist)
print(x.inserted_ids) '''

data = mycollection.find()

print(data) # it sotres the object of the collection.find()

data_all = mycollection.find()

#for d in data_all: # print all the data we created
 #   print(d)

#for d in mycollection.find({},{'address':1}):  # it will exclude the specific data we mention
  #  print(d)

#for d in mycollection.find({},{'_id':1,'name':1}): # give only id and name in output
 #   print(d)
'''''
myquery = {'address':'ad1'}

for d in mycollection.find(myquery):
    print(d)

print("="*30)

for d in mycollection.find().sort('name'): # sort the data
    print(d)


print("="*30)
print("Desending order")
for d in mycollection.find().sort('name',-1): # sort in descending
    print(d) '''


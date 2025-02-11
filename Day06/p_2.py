import pymongo

#print(pymongo.version) # show the version of pymongo

mycn = pymongo.MongoClient("mongodb://localhost:27017/") # connect my mongodb to this server
#mydatabase = mycn["mydb1"]  # create a database as mydb1

#print(mycn.list_database_names()) # connect local database and giving the available databases

if "mydb" in mycn.list_database_names(): # check the database is avilable
    print("database exists")
    mydatabase = mycn["mydb"]

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
mylist = [ {'_id':0,'name':'abc1','address':'ad1'},
           {'_id':1,'name':'abc2','address':'ad2'},
           {'_id':2,'name':'abc3','address':'ad3'}]
x= mycollection.insert_many(mylist)
print(x.inserted_ids)'''

#data = mycollection.find()
#print(data)

#data_all = mycollection.find()

#for d in data_all: # print all the data we created
 #   print(d)

#for d in mycollection.find({},{'address':0}):  # it will exclude the specific data we mention
  #  print(d)

for d in mycollection.find({},{'_id':0,'name':1,'address':1}):
    print(d)
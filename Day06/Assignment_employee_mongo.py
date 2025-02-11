#Implemet employee details in mongodb using oops

import pymongo
mycn = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = mycn["mydb"]

class Employee:
    def __init__(self):
        self.mycol = mydb["employee"]

    def emp_details(self):
        while True:
            print("Employee Details")
            self.id =input("enter employee id")
            self.name = input("enter employee name")
            self.age = input("enter employee age")
            self.salary = input("enter employee salary")
            l1=[{'id':self.id,'name':self.name,'age':self.age,'salary':self.salary}]
            x=self.mycol.insert_many(l1)
            print(x.inserted_ids)
            ch=input("Choose the choice to continue/not Y/N:")
            if ch=='N':
                break
        data = self.mycol.find()
        for x in data:
            print(x)

    def update(self):
        print("update")
        self.id = input("enter employee id")
        query={"id":self.id}
        self.key=input("enter a key to update")
        self.value=input("enter a value to update")
        newquery={'$set':{self.key:self.value}}
        self.mycol.update_one(query,newquery)

    def delete(self):
        print("delete")
        self.id=input("enter employee id to delete")
        query={'id':self.id}
        self.mycol.delete_one(query)

e=Employee()
e.emp_details()
e.update()
e.delete()





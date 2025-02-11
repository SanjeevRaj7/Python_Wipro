import json

class employee:
    def __init__(self):
        self.name=input("Enter employee name: ")
        self.id=input("Enter employee ID: ")
        self.salary=input("Enter employee salary: ")
        d1 = {'id':self.id,'name':self.name,'salary':self.salary}
        self.filepath = "Assignment.json"
        with open(self.filepath, 'w') as f:
            json.dump(self.filepath,f)
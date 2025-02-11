class Employee:
    def __init__(self, name=0, age=0,salary=0,id=0):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

    #getters and setter
    #getters
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getSalary(self):
        return self.salary
    def getId(self):
        return self.id
    #setters
    def setName(self,name):
        self.name = name
    def setAge(self,age):
        self.age = age
    def setSalary(self,salary):
        self.salary = salary
    def setId(self,id):
        self.id = id

    def displayEmployee(self):
        print("="*30)
        print("\tEmployee Details")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.salary)
        print("Id:",self.id)
        print("=" * 30)

    def setEmployee(self,name,age,salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

e1 = Employee()
e1.setEmployee("bhima",45,10000,101)
e1.displayEmployee()

print(e1.getName())
e1.setName("Shankar")
e1.displayEmployee()
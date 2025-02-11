#DUNDER / MAGIC METHODS USED IN CLASSES
#from day02.Assignment2_03 import employees

'''''
def __str__(self):
    return f'fname:{self.fname}, lname:{self.lname}' # using print we print the  values
e=employees
print(e1) it will take as  str and print the values '''
'''''
#using __repr__
 def __repr__:
 return f'Employee {self.name}'
print(repr(e1))'''

class Employee:
    def __init__(self, fname=None, lname=None, salary=None):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def __str__(self):
        return f"""
        fName: {self.fname}
        lName: {self.lname}
        salary: {self.salary}
        """

    def __repr__(self):
        return f"Employee({self.fname}, {self.lname}, {self.salary})"

    def __add__(self, other):
        return self.salary + other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __len__(self):
        return len(self.fname)+len(self.lname)

    def __lt__(self, other):
        return self.fname < other.fname

    def display(self):
        print("fname : ", self.fname)
        print("lname : ", self.lname)
        print("salary : ", self.salary)



e1 = Employee('Amit', 'shankar', 20000)
e1.display()
print(e1)
print(repr(e1))
e2 = Employee('amit', 'Kumar', 20000)

print(e1+e2)

print(e1 == e2)
print(len(e1))
print(e1<e2)


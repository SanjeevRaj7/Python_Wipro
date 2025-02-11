#3
'''Tuple Operations on Employee Data (Tuples & Sets)
Problem Statement: Write a program that processes a list of tuples where each tuple
contains employee details: (EmployeeID, Name, Department). Perform the following
tasks:
1. Extract all unique departments using a set.
2. Count the number of employees in each department using a dictionary '''

details=[(101,'Alice','IT'),(102,'Bob','HR'),(103,'Charlie','IT'),(103,'David','HR'),(104,'Eve','Finance')]
print(details)

employees=set()
employees.update(details)#adding details to employees set
print(employees)
unique_dept=set() #unique department
unique_count={} #unique count

for employee in employees:
    dept=employee[2] # it will take the department from each set
    unique_dept.add(dept)

    if dept not in unique_count: # if department is not there it will add as key and value
        unique_count[dept]=1
    else:
        unique_count[dept]+=1


print(unique_dept)
print(unique_count)
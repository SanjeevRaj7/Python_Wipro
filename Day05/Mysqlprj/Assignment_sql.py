#Implemet employee details in mysql using oops
import mysql.connector


class Employee:
    def __init__(self):
        self.tablename = input("enter a table name: ")

    def createTable(self):
        sqlCmd = f"create table {self.tablename} (id int, name varchar(255), age int,salary int);"
        mycur.execute(sqlCmd)
        mydb.commit()
        print(f"table {self.tablename} created")

    def insert(self):
        while True:
            print("Enter Employee details")
            self.id = int(input("Enter Employee ID: "))
            self.name = input("Enter Employee Name: ")
            self.age = int(input("Enter Employee Age: "))
            self.salary = int(input("Enter Employee Salary: "))
            sqlCmd = f"insert into {self.tablename} (id,name,age,salary) values ({self.id},'{self.name}',{self.age},{self.salary});"
            mycur.execute(sqlCmd)
            ch = input("Do you want to continue? (y/n): ")
            if ch == "n":
                mydb.commit()
                break
                print(f"employee {self.name} inserted successfully")

    def readall(self):
        sqlCmd = f"select * from {self.tablename}"
        mycur.execute(sqlCmd)
        records = mycur.fetchall()
        for x in records:
            print(x)

    def update(self):
        print("Update Records")
        self.id = int(input("Enter Employee ID: "))
        self.field = input("Enter Employee Field to update: ")
        self.value = input("Enter a value to update: ")

        sqlCmd = f"update {self.tablename} set {self.field} ='{self.value}' where id={self.id}"
        mycur.execute(sqlCmd)
        mydb.commit()

    def remove(self):
        print("Remove Records")
        self.id = int(input("Enter Employee ID: "))
        sqlCmd = f"delete from {self.tablename} where id={self.id}"

        mycur.execute(sqlCmd)
        mydb.commit()


if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="localhost",
        user='Sanjeev',
        password="Silusanju@123",
        database="mydb2"
    )

mycur = mydb.cursor()
e=Employee()
e.createTable()
e.insert()
e.readall()
e.update()
e.remove()


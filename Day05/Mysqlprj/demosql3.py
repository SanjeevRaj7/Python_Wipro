#GET EMPLOYEE DETAILS AND PRINT DETAILS THAT ALREADY EXIST

import mysql.connector


def createTable(mycur, myTab):
    sqlCmd = f"create table {myTab} (id int, name varchar(255), age int)"
    mycur.execute(sqlCmd)
    mydb.commit()

def insertOne(mycur, myTab):
    print("Enter Employee details")
    id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    sqlCmd = f"insert into {myTab} (id, name,age) values (%s, %s, %s)"
    data = (id, name, age)
    mycur.execute(sqlCmd, data)
    mydb.commit()

def insertMany(mycur, myTab):
    sqlCmd = f"insert into {myTab} (id, name,age) values (%s, %s, %s)"
    data = [
        (1,'abc1',1),
        (2,'abc2',2),
        (3,'abc3',3)
    ]
    mycur.executemany(sqlCmd, data)
    mydb.commit()

def readAll(mycur, myTab):
    sqlCmd = f"select * from {myTab}"
    mycur.execute(sqlCmd)
    myresult = mycur.fetchall()

    for rec in myresult:
        print(rec)

def searchRec(mycur, myTab):
    id = int(input("Enter Employee ID: "))
    sqlCmd = f"select * from {myTab} where id={id}"
    mycur.execute(sqlCmd)
    res = mycur.fetchall()
    for rec in res:
        print(rec)

def updateOne(mycur, myTab):
    print("Update Records")
    id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")

    sqlCmd = f"update {myTab} set name='{name}' where id={id}"
    mycur.execute(sqlCmd)
    mydb.commit()

def removeRec(mycur, myTab):
    print("Remove Records")
    id = int(input("Enter Employee ID: "))
    sqlCmd = f"delete from {myTab} where id={id}"

    mycur.execute(sqlCmd)
    mydb.commit()

if __name__ == "__main__":
    dbName = input("Enter the database name: ")
    mydb = mysql.connector.connect(
        host="localhost",
        user='Sanjeev',
        password="Silusanju@123"
    )

    mycur = mydb.cursor()
    sqlCmd = "CREATE DATABASE IF NOT EXISTS " + dbName
    mycur.execute(sqlCmd)
    mycur.execute("use " + dbName)
    tabName = input("Enter the table name: ")
   # createTable(mycur, tabName)
    insertOne(mycur, tabName)
    #insertMany(mycur, tabName)
    readAll(mycur, tabName)
    searchRec(mycur, tabName)
    updateOne(mycur, tabName)
    removeRec(mycur, tabName)



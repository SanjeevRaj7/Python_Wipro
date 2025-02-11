#USING READ METHOD we will print all details in pycharm terminal

import pymysql

def createTable(tableName):
    sqlCmds = f'create table {tableName} (id int, name varchar(255), age int, gender varchar(1));'

    try:
        mycur.execute(sqlCmds)
    except pymysql.err.OperationalError as e:
        print("Table already exists")



def insertValue(tableName):
    while True:
        print("Enter the details of Employees:")
        id = int(input("ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender (M/F/T): ")


        sqlCmds = f"insert into {tableName} (id, name, age, gender) values ({id},'{name}',{age},'{gender}')"
        mycur.execute(sqlCmds)
        mycur.execute("commit")

        ch = input("Do you want to continue (Y/N): ")
        if ch == "N" or ch == "n":
            mycur.execute("COMMIT;")
            break


def insertMany(tableName):

    sqlCmds = f"insert into {tableName} (id,name,age,gender) values (%s, %s ,%s, %s)"
    data =[
        (104,'abc3',23,'M'),
        (105, 'abc4', 24, 'F'),
        (106, 'abc5', 25, 'M')
    ]

    mycur.executemany(sqlCmds, data)
    mycur.execute("COMMIT;")
    print(mycur.rowcount,"was inserted." )


def readTable(tableName):
    sqlCmds = f"select * from {tableName}"

    mycur.execute(sqlCmds)

    myresult = mycur.fetchall()

    for rec in myresult:
        print(rec)


def searchRec(tableName):
    id = int(input("ID to be searched: "))
    sqlCmds = f"select * from {tableName} where id ={id}"
    mycur.execute(sqlCmds)
    myresult = mycur.fetchall()

    for rec in myresult:
        print(rec)


mydb = pymysql.connect(
    host="localhost",
    user="Sanjeev",
    password="Silusanju@123",
    database="mydb2"
)

mycur = mydb.cursor()
#mycur.execute("create database mydb2")
mytable = input("Enter the table name: ")
createTable(mytable)
insertValue(mytable)
insertMany(mytable)

readTable(mytable)
searchRec(mytable)
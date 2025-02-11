#9
#Write a Python script to connect to a MySQL database, create a new table, insert some data, and retrieve it using a parameterized query.

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="Sanjeev", passwd="Silusanju@123", database="mydb2")
mycur = mydb.cursor()
table = input("Enter the table name: ")
s= f"create table {table} (id int, name varchar(255), dept varchar(20))"
mycur.execute(s)
mydb.commit()
s=f"insert into {table}(id,name,dept) values(%s,%s,%s)"
data =[(1,'Sanjeev','IT'),(2,'sanjay','Design'),(3,'Ajay','IT')]
mycur.executemany(s,data)

dept="IT"
s=f"select * from {table} where dept =%s"

mycur.execute(s,(dept,))
x=mycur.fetchall()
for i in x:
    print(i)




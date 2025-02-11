#TO SHOW DATABASES
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="Sanjeev",password="Silusanju@123",)
mycur=mydb.cursor()
mycur.execute("show databases")

for x in mycur:
    print(x)

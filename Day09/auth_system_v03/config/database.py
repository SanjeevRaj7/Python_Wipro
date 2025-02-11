import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="bhima",
        password="bhima123",
        database="mydb"
    )

#this files handles MySQL DB conn

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="bhima",
        passwd="bhima123",
        database="mydb"
    )


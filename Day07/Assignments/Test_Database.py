#7
#Write a Pytest test case that uses fixtures to set up a temporary database for testing.


import pytest
import mysql.connector

@pytest.fixture
def db():
    con = mysql.connector.connect(
        host = "localhost",
        user = "Sanjeev",
        password = "Silusanju@123",
        database = "mydb2" )
    cur=con.cursor()
    #create
    sqlcmd = f"create table user (name varchar(20),age int)"
    cur.execute(sqlcmd)
    #insert
    sqlcmd = f"insert into user(name,age) values(%s,%s)"
    data=[('sanjeev',21),('sanjay',21),('ajay',21)]
    cur.executemany(sqlcmd,data)
    con.commit()
    yield con # making the database to test
    #clean
    cur.execute("drop table user")

def test_db(db):
    mycur = db.cursor()
    mycur.execute("select * from user")
    r= mycur.fetchall()

    assert len(r) == 3
    assert r[0] == ('sanjeev',21)
    assert r[1] == ('sanjay',21)



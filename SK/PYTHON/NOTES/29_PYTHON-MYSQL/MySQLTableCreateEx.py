#Program for creatinga table in a Database
#MySQLTableCreateEx.py
import mysql.connector
def tablecreate():
    try:
        con=mysql.connector.connect(host="127.0.0.1",
                                    user="root",
                                    passwd="root",
                                    database="batch11am")
        cur=con.cursor()
        #create a table employee in batch11am
        tq="create table student(sno int primary key,name varchar(10) not null ,marks float not null)"
        cur.execute(tq)
        print("Table create in batch11 database in MySQL--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL:",db)
#Main Program
tablecreate() # Function call
#Program for Creating a Database on the name of batch11am
#MySQLDatabaseCreateEx.py
import mysql.connector
def databasecreate():
    try:
        con=mysql.connector.connect(host="127.0.0.1",
                                    user="root",
                                    passwd="root")
        cur=con.cursor()
        #create the data base as batch11am in mysql
        dc="create database batch9am"
        cur.execute(dc)
        print("Database Created in MySQL--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL:",db)
#Main Program
databasecreate() # Function call
#Program for Cdroping a Database from mysql
#MySQLDatabaseDropEx.py
import mysql.connector
def databasedrop():
    try:
        con=mysql.connector.connect(host="127.0.0.1",
                                    user="root",
                                    passwd="root")
        cur=con.cursor()
        #drop the data base from mysql
        cur.execute("drop database kvr")
        print("Database droped from MySQL--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL:",db)
#Main Program
databasedrop() # Function call
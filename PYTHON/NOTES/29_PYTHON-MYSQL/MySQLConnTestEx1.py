#Program for Demonstrating How to get the connection from MySQL
#MySQLConnTestEx1.py
import mysql.connector
try:
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="root")
    print("Python Program Got Connection from MySQL")
    cur=con.cursor()
    print("Python Program Created Cursor Object")
except mysql.connector.DatabaseError as db:
    print("Problem in MySQL:",db)

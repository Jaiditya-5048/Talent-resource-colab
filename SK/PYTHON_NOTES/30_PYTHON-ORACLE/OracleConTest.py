#Program for Demonstrating How to get the connection from Oracle db
#OracleConTest.py
import oracledb as orc # Step-1
try:
    con=orc.connect("system/tiger@localhost/orcl") # Step-2
    print("Type of con=",type(con))
    print("Python Program Obtains Connection from Oracle DB")
    print("------------------------------------------------")
except orc.DatabaseError as db:
    print("Problem in Oracle:", db)
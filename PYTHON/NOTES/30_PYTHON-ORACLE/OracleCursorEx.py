#Program for Demonstrating How to create Cursor Object
#OracleCursorEx.py
import oracledb as orc
try:
    conobj=orc.connect("system/tiger@localhost/orcl") # Step-2
    print("Type of conobj=",type(conobj))
    print("Python Program Obtains Connection from Oracle DB")
    print("------------------------------------------------")
    curobj=conobj.cursor() # Step-3
    print("Type of curobj=",type(curobj))
    print("Python Program created cursor object")
    print("------------------------------------------------")
except orc.DatabaseError as db:
    print("Problem in Oracle DB:",db)

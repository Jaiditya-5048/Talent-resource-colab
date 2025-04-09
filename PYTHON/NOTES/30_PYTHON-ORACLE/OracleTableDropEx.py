#Program for Removing the Table from Oracle database
#OracleTableDropEx.py
import oracledb as orc # Step-1
def tableremove():
    try:
        con=orc.connect("system/tiger@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        dq="drop table %s" %(input("Enter Table Name to Remove:"))
        cur.execute(dq)
        #Step-5
        print("Table Removed Sucessfully in Oracle--verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)

#Main Program
tableremove()
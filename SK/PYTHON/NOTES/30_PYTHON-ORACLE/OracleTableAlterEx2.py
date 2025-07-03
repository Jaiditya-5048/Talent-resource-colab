#Program for altering employee table by adding new col name
#OracleTableAlterEx2.py
import oracledb as orc # Step-1
def tablealter():
    try:
        con=orc.connect("system/tiger@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        aq="alter table employee add(compname varchar2(10) not null)"
        cur.execute(aq)
        #Step-5
        print("Table Columns altered Sucessfully in Oracle--verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)

#Main Program
tablealter()

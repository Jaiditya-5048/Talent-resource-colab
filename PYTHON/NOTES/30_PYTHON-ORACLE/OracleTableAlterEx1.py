#Program for altering employee table column sizes
#OracleTableAlterEx1.py
import oracledb as orc # Step-1
def tablealter():
    try:
        con=orc.connect("system/tiger@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        aq="alter table employee modify(eno number(3),name varchar2(15))"
        cur.execute(aq)
        #Step-5
        print("Table Columns altered Sucessfully in Oracle--verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)

#Main Program
tablealter()

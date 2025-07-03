#Program for Creating a Table employee with Col Names
#OracleTableCreateEx.py
import oracledb as orc # Step-1
def tablecreate():
    try:
        con=orc.connect("system/tiger@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        tc="create table employee(eno number(3) primary key,name varchar2(10) not null,sal number(5,2) not null, compname varchar2(10) not null)"
        cur.execute(tc)
        #Step-5
        print("Table Created Sucessfully in Oracle--verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)

#Main Program
tablecreate()

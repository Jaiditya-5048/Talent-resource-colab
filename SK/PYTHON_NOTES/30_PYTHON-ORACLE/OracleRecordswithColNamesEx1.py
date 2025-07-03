#Program for Reading all records for Table with Col Names
#OracleRecordswithColNamesEx1.py
import oracledb as orc
def recordscolnames():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        #Query
        sq="select * from employee order by sal DESC"
        cur.execute(sq)
        #To get Col Names
        print("-"*50)
        colinfo=cur.description
        for col in colinfo:
            print(col[0],end="\t")
        print()
        print("-" * 50)
        #Get the Records
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val), end="\t")
            print()
        print("-" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)

#Main Program
recordscolnames() # Function Call
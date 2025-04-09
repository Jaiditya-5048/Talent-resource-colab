#Program for Obtaining Complete Records with Col names of any table which is obtained from KBD
#OracleRecordsTable.py
import oracledb as orc
def recordscolnames():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        #Query
        sq="select * from %s" %input("Enter Table Name to view Records:")
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
        print("Table Does not Exist")

#Main Program
recordscolnames() # Function Call
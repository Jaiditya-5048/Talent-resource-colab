#Program for Reading all records for Table with Col Names
#MySQLRecordswithTableEx1.py
import mysql.connector
def recordscolnames():
    try:
        con = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      passwd="root",
                                      database="batch11am")
        cur=con.cursor()
        #Query
        sq="select * from %s " %(input("Enter Table Name:"))
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
        if(len(records)==0):
            print("Table Does not contain records")
        else:
            for record in records:
                for val in record:
                    print("{}".format(val), end="\t")
                print()
        print("-" * 50)
    except mysql.connector.DatabaseError as db:
        print("Problem in mysql:",db)

#Main Program
recordscolnames() # Function Call
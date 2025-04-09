#Program for Reading the Data from CSV File in tabular format
#CSVReadEx2.py
import csv
with open("E:\\KVR-PYTHON-11AM\\CSV\\NOTES\\student.csv") as fp:
    csvr=csv.reader(fp) # here csvr is an object <class, _csv.reader>
    print("------------------------------------------")
    for record in csvr:# here record is of type list
        for val in record:
            print("\t{}".format(val),end=" ")
        print()
    print("------------------------------------------")

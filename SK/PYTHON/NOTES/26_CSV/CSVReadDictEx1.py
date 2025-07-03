#Program for Reading the Data from CSV File in the form Dict
#CSVReadDictEx1.py
import csv
with open("E:\\KVR-PYTHON-11AM\\CSV\\NOTES\\EMPLOYEES.csv") as fp:
    csvdr=csv.DictReader(fp) # here csvdr is ab object of <class 'csv.DictReader'>
    for record in csvdr: # here record is of type <class, dict>
        print("------------------------------------")
        for key,value in record.items():
            print("\t{}--->{}".format(key,value))
        print("------------------------------------")
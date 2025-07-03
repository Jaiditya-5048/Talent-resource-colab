#prohgram for Reading the Data from CSV File
#NON-CSVReadEx1.py
with open("E:\\KVR-PYTHON-11AM\\CSV\\NOTES\\EMPLOYEES.csv") as fp:
    csvdata=fp.read()
    print("----------------------------------")
    print(csvdata)
    print("----------------------------------")
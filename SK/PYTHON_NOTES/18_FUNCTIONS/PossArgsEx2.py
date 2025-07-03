#Program for Demonstrating Possitional Arguments
#PossArgsEx2.py
def  dispstuddata(sno,name,marks,crs):
    print("\t{}\t\t{}\t\t\t{}\t\t{}".format(sno,name,marks,crs))

#Main Program
print("-"*50)
print("\tSNO\t\tNAME\t\tMARKS\t\tCOURSE")
print("-"*50)
dispstuddata(100,"RS",55.55,"PYTHON") # function call
dispstuddata(200,"TR",66.66,"PYTHON")  # function call
dispstuddata(300,"SS",62.62,"PYTHON")  # function call
dispstuddata(400,"SS",44.44,"PYTHON") #Function Call
print("-"*50)


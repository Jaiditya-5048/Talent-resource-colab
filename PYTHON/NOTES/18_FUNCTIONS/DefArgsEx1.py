#Program for Demonstrating Default ASrguments
#DefArgsEx1.py
def  dispstuddata(sno,name,marks,crs="PYTHON"):
    print("\t{}\t\t{}\t\t\t{}\t\t{}".format(sno,name,marks,crs))

#main Program
print("-"*50)
print("\tSNO\t\tNAME\t\tMARKS\t\tCOURSE")
print("-"*50)
dispstuddata(100,"RS",55.55) # function call
dispstuddata(200,"TR",66.66)  # function call
dispstuddata(300,"SS",62.62)  # function call
dispstuddata(400,"SS",44.44) #Function Call
print("-"*50)
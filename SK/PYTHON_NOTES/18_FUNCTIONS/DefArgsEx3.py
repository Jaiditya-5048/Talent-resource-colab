#Program for Demonstrating Default ASrguments
#DefArgsEx2.py
def  dispstuddata(sno,name,marks,crs="PYTHON",city="HYD"):
    print("\t{}\t\t{}\t\t\t{}\t\t{}\t\t{}".format(sno,name,marks,crs,city))

#main Program
print("-"*50)
print("\tSNO\t\tNAME\t\tMARKS\t\tCOURSE\t\tCITY")
print("-"*50)
dispstuddata(100,"RS",55.55) # function call
dispstuddata(200,"TR",66.66)  # function call
dispstuddata(300,"SS",62.62)  # function call
dispstuddata(400,"SS",44.44) #Function Call
dispstuddata(500,"SR",55.55,"JAVA")
dispstuddata(600,"MC",15.55)
dispstuddata(700,"KN",94.56,city="BANG")
dispstuddata(800,"KV",11.11,city="AP",crs="Dajngo")
dispstuddata(900,"CH",99.56)
dispstuddata(crs="C",sno=750,city="USA",name="TR",marks=22.22)

print("-"*50)
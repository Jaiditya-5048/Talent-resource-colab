#Program for Demonstrating Possitional Arguments
#PossArgsEx1.py
def  dispstuddata(sno,name,marks):
    print("\t{}\t\t{}\t\t\t{}".format(sno,name,marks))

#Main Program
print("-"*50)
print("\tSNO\t\tNAME\t\tMARKS")
print("-"*50)
dispstuddata(100,"RS",55.55) # function call
dispstuddata(200,"TR",66.66)  # function call
dispstuddata(300,"SS",62.62)  # function call
dispstuddata(400,"SS",44.44) #Function Call
print("-"*50)


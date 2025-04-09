#Program accepting a Digit and Display Its name
#SimpleIfStmtEx4.py
d=int(input("Enter a Digit:")) # d=0 1 2 3 4 5 6 7 8 9    689
if(d==0):
    print('{} is Zero'.format(d))
if(d==1):
    print("{} is ONE".format(d))
if(d==2):
    print("{} is TWO".format(d))
if(d==3):
    print("{} is THREE".format(d))
if(d==4):
    print("{} is FOUR".format(d))
if(d==5):
    print("{} is FIVE".format(d))
if(d==6):
    print("{} is SIX".format(d))
if(d==7):
    print("{} is SEVEN".format(d))
if(d==8):
    print("{} is EIGHT".format(d))
if(d==9):
    print("{} is NINE".format(d))
if (-9<=d<0):
    print("{} is -Ve Digit:".format(d))
if (d>9) or (d<-9):
     print("{} is Number:".format(d))
print("Program Execution Completed")
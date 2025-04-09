#Program for Demonstrating How to use break keyword
#BreakStmtEx4.py
s="MISSISSIPPI"
#Requirement is ---to display--MISS
for index,value in enumerate(s):
    if(index==4):
        break
    print(value,end="")



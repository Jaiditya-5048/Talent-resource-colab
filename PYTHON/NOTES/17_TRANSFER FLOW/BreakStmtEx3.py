#Program for Demonstrating How to use break keyword
#BreakStmtEx3.py
s="MISSISSIPPI"
#Requirement is ---to display--MISS
ctr=0
for ch in s:
    if(ch=="I"):
        ctr+=1
    if(ctr==2):
        break
    print(ch,end="")
print()
print("Program exeuction completed")

#Program for Demonstrating How to use break keyword
#BreakStmtEx2.py
s="PYTHON"
print("By using while loop")
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("else part of while loop")
print("-----------------------------------")
#My Requirment--to display-- PYTH  without using Indexing and slicing
i=0
while(i<len(s)):
    if(s[i]=="O"):
        break
    print(s[i],end="")
    i+=1
else:
    print("else part of while loop")
print()
print("Program Execution Completed")
print("This is called Logicall Termination")
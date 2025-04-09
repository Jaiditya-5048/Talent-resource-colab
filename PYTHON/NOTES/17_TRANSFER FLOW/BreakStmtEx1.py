#Program for Demonstrating How to use break keyword
#BreakStmtEx1.py
s="PYTHON"
print("By using for loop")
for val in s:
    print(val)
else:
    print("else part of for loop")
print("=========================================")
#My Requirment--to display-- PYTH  without using Indexing and slicing
print("By using for loop")
for ch in s:  # s= "PYTHON"
    if(ch=="O"):
        break
    print(ch,end="")
else:
    print("else part of for loop")
print()
print("Program Execxution completed")




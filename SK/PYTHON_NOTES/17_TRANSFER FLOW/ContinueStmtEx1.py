#Program for Demonstrating continue statement.
#ContinueStmtEx1.py
s="PYTHON"
print("By using for loop")
for ch in s:
    print(ch)
else:
    print("else part of for loop")
print("----------------------------------")
#My Requirment is--to display-- PYHON
for ch in s:
    if(ch=="T"):
        continue
    print(ch)
else:
    print("else part of for loop")
print("----------------------------------")
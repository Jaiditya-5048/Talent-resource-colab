#Program for Demonstrating continue statement.
#ContinueStmtEx3.py
s="PYTHON"
print("By using for loop")
for ch in s:
    print(ch)
else:
    print("else part of for loop")
print("----------------------------------")
#My Requirment is--to display-- PYHN
for ch in s:
    if ch in ["T","O"]:
        continue
    print(ch)
else:
    print("else part of for loop")
print("----------------------------------")
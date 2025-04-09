#Program displaying special symbols from Line of Text
#ContinueStmtEx9.py
line=input("Enter a Line of Text:")#line=Apple
for ch in line:
    if (not ch.isdigit()) and (not ch.isalnum()):
        print(ch)
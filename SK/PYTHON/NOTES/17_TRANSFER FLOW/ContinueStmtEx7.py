#Program displaying consonants from Line of Text
#ContinueStmtEx7.py
line=input("Enter a Line of Text:")#line=Apple
for ch in line.lower():
    if (ch=="a") or (ch=="e") or (ch=="i")or (ch=="o") or (ch=="u") or (ch.isdigit()) or (ch.isspace()):
        continue
    print(ch)
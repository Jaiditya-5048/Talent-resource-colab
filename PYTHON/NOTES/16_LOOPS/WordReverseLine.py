#WordReverseLine.py
line=input("Enter a Line of Text:")
lst=[]
for word in line.split():
    lst.append(word[::-1])
print(" ".join(lst))
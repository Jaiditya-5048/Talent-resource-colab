#Program for accepting a Word OR Line of Text and display every Character
#ForLoopEx1.py
s="PYTHON"
print("By using For Loop--FD without Index")
for ch in s:
    print(ch)
print("By using For Loop--BD with out Index")
for ch in s[::-1]:
    print(ch)
print("-----------OR---------------------")
print("By using For Loop--FD with +VE Index")
for i in range(len(s)):
    print(s[i])
print("-----------OR---------------------")
print("By using For Loop--FD with -VE Index")
for i in range(-6,0):
    print(s[i])
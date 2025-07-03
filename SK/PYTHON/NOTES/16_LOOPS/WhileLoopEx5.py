#Program for accepting a Word OR Line of Text and display every Character
#WhileLoopEx5.py
s="PYTHON"
print("By using while Loop--Logic-1-+VE-FD")
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
print("-------------OR----------------")
print("By using while Loop--Logic-2->-VE-FD")
i=-len(s)
while(i<=-1):
    print(s[i])
    i=i+1
print("-------------OR----------------")
print("By using while Loop--Logic-3-+VE-BD")
i=len(s)-1
while(i>=0):
    print(s[i])
    i=i-1
print("-------------OR----------------")
print("By using while Loop--Logic-4-->-VE-BD")
i=-1
while(i>=-len(s)):
    print(s[i])
    i=i-1
print("-------------OR----------------")
print("By using while Loop--Logic-5-+VE-FD")
s=input("Enter a Value:")
s=s[::-1]
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
print("==============================")
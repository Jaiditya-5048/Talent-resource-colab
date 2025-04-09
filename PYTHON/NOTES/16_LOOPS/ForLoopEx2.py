#Program displaying the Values of List
#ForLoopEx2.py
lst=[10,"Rossum",45.67,True,2+3j]
print("--------------------------------")
print("By using while loop--Logic-1--FD")
print("--------------------------------")
i=0
while(i<len(lst)):
    print(lst[i])
    i=i+1
print("--------------------------------")
print("By using for loop--Logic-2--FD")
print("--------------------------------")
for val in lst:
    print(val)
print("--------------------------------")
print("By using for loop--Logic-3 with Index--FD")
print("--------------------------------")
for i in range(len(lst)):
    print(lst[i])
print("--------------------------------")
print("By using for loop--Logic-3 with -ve Index--FD")
print("--------------------------------")
for i in range(-len(lst),0):
    print(lst[i])
print("--------------------------------")
print("By using for loop--Logic-3 with -ve Index--BD")
print("--------------------------------")
for i in range(-1,-len(lst)-1,-1):
    print(lst[i])
print("--------------------------------")
print("By using for loop--Logic-3 without--BD")
print("--------------------------------")
for val in lst[::-1]:
    print(val)
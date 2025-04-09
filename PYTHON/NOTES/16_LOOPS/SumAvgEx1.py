#Program finding aum and avg of List of Values--don't use sum()
#SumAvgEx1.py
lst=[10,2,20,30,40,15]  # Fixed Data
s=0
print("-----------------------------")
for val in lst:
    print(val)
    s+=val
else:
    print("-----------------------------")
    print("Sum={}".format(s))
    print("Avg=",(s/len(lst)))
    print("-----------------------------")

#InnerLoopEx4.py---while loop in for loop
for i in range(1,6): # Outer for loop
    print("="*50)
    print("Outer Loop i={}".format(i))
    j = 3
    while (j >=1):  # Inner Loop
        print("\tInner loop j={}".format(j))
        j = j - 1
    else:
        print("Out-off inner loop")
        print("------------------------")
else:
    print("Out-off outer loop")
    print("=" * 50)
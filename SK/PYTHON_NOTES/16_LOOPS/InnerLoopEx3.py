#InnerLoopEx3.py----for loop in while loop
i=5
while(i>=1): # Outer loop
    print("=" * 50)
    print("Outer Loop i={}".format(i))
    i=i-1
    for j in range(3,0,-1):  # Inner loop
        print("\tInner loop j={}".format(j))
    else:
        print("Out-off inner loop")
        print("------------------------")
else:
    print("Out-off outer loop")
    print("------------------------")
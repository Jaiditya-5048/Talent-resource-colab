#InnerLoopEx1.py
for i in range(1,6): # Outer for loop
    print("="*50)
    print("Outer Loop i={}".format(i))
    for j in range(1,4): # Inner loop
        print("\tInner loop j={}".format(j))
    else:
        print("Out-off inner loop")
        print("------------------------")
else:
    print("Out-off outer loop")
    print("=" * 50)
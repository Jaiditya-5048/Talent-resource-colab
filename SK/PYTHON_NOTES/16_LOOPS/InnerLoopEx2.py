#InnerLoopEx2.py
i=1
while(i<6): # Outer loop
    print("=" * 50)
    print("Outer Loop i={}".format(i))
    j=1
    while(j<4): # Inner Loop
        print("\tInner loop j={}".format(j))
        j=j+1
    else:
        print("Out-off inner loop")
        print("------------------------")
        i=i+1
else:
    print("Out-off outer loop")
    print("------------------------")
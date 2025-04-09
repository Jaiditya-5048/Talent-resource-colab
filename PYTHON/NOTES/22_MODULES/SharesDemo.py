#SharesDemo.py-----Viewer Program---Main Program
import Shares,time,importlib
def dispshares(d):
    print("="*50)
    print("ShareName\t\tShareValue")
    print("=" * 50)
    for shn,ssv in d.items():
        print("\t{}\t\t{}".format(shn,ssv))
    print("=" * 50)

#Main Program
d=Shares.sharesinfo()
dispshares(d)
print("I am going to Sleep for 20 Seconds")
time.sleep(20)
print("I am coming out-off of Sleep  after 20 Seconds")
importlib.reload(Shares) # Used for Re-Loading Previously imported module for obtaining New values
d=Shares.sharesinfo()
dispshares(d)
print("I am going to Sleep for 20 Seconds")
time.sleep(20)
print("I am coming out-off of Sleep  after 20 Seconds")
importlib.reload(Shares) # Used for Re-Loading Previously imported module for obtaining New values
d=Shares.sharesinfo()
dispshares(d)
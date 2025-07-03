##Program for Showing The Dead Lock Avoidence
#SynchEx1.py
import threading,time
def  multable(n):
	#Acquire the Lock
	L.acquire() # Step-2
	if(n<=0):
		print("{}-->{} Invalid Input".format(threading.current_thread().name,n))
	else:
		print("-"*50)
		print("{}--->Mul Table for {}".format(threading.current_thread().name,n))
		print("-"*50)
		for i in range(1,11):
			print("\t{} x {} = {}".format(n,i,n*i))
			time.sleep(0.25)
		print("-"*50)
	#Release the Lock
	L.release() # Step-3
 	
#Main Program
#Create the Lock
L=threading.Lock() # Here L is an object of Lock Class--Step-1
#Create Four Sub Threads and all of them are targetted to same Function.
t1=threading.Thread(target=multable,args=(10,))
t2=threading.Thread(target=multable,args=(-15,))
t3=threading.Thread(target=multable,args=(19,))
t4=threading.Thread(target=multable,args=(9,))
#dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()



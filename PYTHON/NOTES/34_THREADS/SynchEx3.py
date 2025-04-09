#SynchEx3.py
import threading,time
def  reservation(rseats):
	L.acquire() # Step-2
	global totalseats
	if(rseats>totalseats):
		print("\tHi {},  {} Seats are Not Available--try next.. ".format(threading.current_thread().name,rseats))
		time.sleep(2)
	else:
		totalseats=totalseats-rseats
		print("\tHi {}, {} Seats Reserved Hpy Journey".format(threading.current_thread().name,rseats))
		time.sleep(2)
		print("\tRemaining Seats:{}".format(totalseats))
		if(totalseats==0):
			print("\tTrains is FULL")
		time.sleep(1)
	L.release() # Step-3

#Main Program
totalseats=16
L=threading.Lock() # Step-1
#Create sub Threads
t1=threading.Thread(target=reservation,args=(2,))
t1.name="RS"
t2=threading.Thread(target=reservation,args=(15,))
t2.name="TR"
t3=threading.Thread(target=reservation,args=(10,))
t3.name="DR"
t4=threading.Thread(target=reservation,args=(3,))
t4.name="RS"
t5=threading.Thread(target=reservation,args=(2,))
t5.name="SS"
t6=threading.Thread(target=reservation,args=(1,))
t6.name="KV"
#Dispatch the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
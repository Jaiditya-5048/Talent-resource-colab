#SynchEx2.py
import threading,time
def  clearcheck(camt):
	L.acquire() # Step-2
	global vmacbal
	if(camt>vmacbal):
		print("\tHi {}, INR {} Valued Check is Bounced-contact... ".format(threading.current_thread().name,camt))
		time.sleep(2)
	else:
		vmacbal=vmacbal-camt
		print("\tHi {},  INR {} Valued Check is Cleared".format(threading.current_thread().name,camt))
		time.sleep(2)
		print("\tRemaining Account Balance:{}".format(vmacbal))
		if(vmacbal==0):
			print("\tAccount contains ZERO Balance")
		time.sleep(1)
	L.release() # Step-3

#Main Ptogram
vmacbal=2500
L=threading.Lock() # Step-1
#Create sub Threads
t1=threading.Thread(target=clearcheck,args=(2000,))
t1.name="RS"
t2=threading.Thread(target=clearcheck,args=(1500,))
t2.name="TR"
t3=threading.Thread(target=clearcheck,args=(3000,))
t3.name="DR"
t4=threading.Thread(target=clearcheck,args=(500,))
t4.name="RS"
t5=threading.Thread(target=clearcheck,args=(100,))
t5.name="SS"
#Dispatch the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

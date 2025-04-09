#Program for Showing Internal Flow of MainTherad  along  Sub Threads with Time 
#MainThreadWithSubThreadsInternalFlowWithTime.py
import threading,time
def squares(lst):
	for val in lst:
		print("{}--->square({})={}".format(threading.current_thread().name,val,val**2))
		time.sleep(1)

def cube(lst):
	for val in lst:
		print("{}--->cube({})={}".format(threading.current_thread().name,val,val**3))
		time.sleep(1)

#Main Program
bt=time.time()
print("Program Execution Started by:{}".format(threading.current_thread().name)) # MainThread
lst=[12,6,7,-4,18,16,25,2,-5]
#Create Sub Threads
t1=threading.Thread(target=squares, args=(lst,) )
t2=threading.Thread(target=cube, args=(lst,) )
#dispatch the sub threads
t1.start()
t2.start()
#Join the Sub Threads
print("Number of Threads in this Program during execution=",threading.active_count())
t1.join()
t2.join()
print("Program Execution Ended by:{}".format(threading.current_thread().name)) # MainThread
et=time.time()
print("Number of Threads in this Program after complete execution=",threading.active_count())
print("Total Execution Time of this Program-with only Main Thread={}".format(et-bt))
#Program for Showing Internal Flow of MainTherad Only with Time (No Sub Threads)
#MainThreadInternalFlowWithTime.py
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
squares(lst)
print("-------------------------------------------")
cube(lst)
print("Program Execution Ended by:{}".format(threading.current_thread().name)) # MainThread
et=time.time()
print("Total Execution Time of this Program-with only Main Thread={}".format(et-bt))
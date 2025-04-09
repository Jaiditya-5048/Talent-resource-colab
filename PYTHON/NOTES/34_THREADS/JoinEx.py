#Program for Demonstrating Thread() and start() and is_alive() and join()
#JoinEx.py
import threading,time
def welcome():
	print("welcome() executed by {}".format(threading.current_thread().name))
	time.sleep(10)
	print("{} is coming out-off Sleep".format(threading.current_thread().name))

def hello(val):
	print("{}, Good Morning".format(val))
	print("hello() executed by {}".format(threading.current_thread().name))
	time.sleep(10)
	print("{} is coming out-off Sleep".format(threading.current_thread().name))
	

#Create sub threads
print("------------------------------------------------------------------")
print("Program Execution started by :{}".format(threading.current_thread().name))
print("------------------------------------------------------------------")
t1=threading.Thread(target=welcome)
t2=threading.Thread(target=hello,args=("Rossum",))
print("Is sub thread under execution before start()=",t1.is_alive())
print("Is sub thread under execution before start()=",t2.is_alive())
#dispatch the sub threads
t1.start()
t2.start()
print("Is sub thread1 under execution=",t1.is_alive())
print("Is sub thread2 under execution=",t2.is_alive())
print("Total Threads Under Execution=", threading.active_count())
#make the MainThread to wait until sub threads joins with MainThread
t1.join()
t2.join()
print("------------------------------------------------------------------")
print("Is sub thread1 under execution after join=",t1.is_alive())
print("Is sub thread2 under execution after join=",t2.is_alive())
print("Total Threads Under Execution after joining all sub threads=", threading.active_count())
print("------------------------------------------------------------------")
print("Program Execution ended by :{}".format(threading.current_thread().name))
print("------------------------------------------------------------------")
#Program for demonstrating current_thread() and active_count()
#CurrentThreadEx1.py
import threading
t=threading.current_thread()
print("Default Thread Info=",t) #  <_MainThread(MainThread, started 19136)>
print("Default Thread Name=",t.name) # MainThread
print("------------------------OR-------------------------------")
print("Default Thread Name=",threading.current_thread().name) # MainThread
print("Number of Active Threads in This Program=",threading.active_count()) # 1
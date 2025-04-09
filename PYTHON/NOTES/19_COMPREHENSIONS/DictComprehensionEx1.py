#Program for Demonstrating the DictComprehension
#DictComprehensionEx1.py
lst=[10,2,13,4,-5,11,-6,18]
dsqlist={ val:val**2   for val in lst }  #----------DictComprehension
print("Original  Elements=",lst) # 
print("Square Dict Elements=",dsqlist) 
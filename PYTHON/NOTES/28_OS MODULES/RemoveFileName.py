#RemoveFileName.py
import os
try:
    os.remove("E:\\KVR-PYTHON-4PM\\OPERATORS\\notes\\BITWISE OP\\SwapWithBitwise.py")
    print("File Removed--verify")
except FileNotFoundError:
    print("File Name does not exist")
import time
import gc
import sys
class test:
    def __init__(self):
        print("object initialization")
t1=test()
t2=t1
print(sys.getrefcount(t2))


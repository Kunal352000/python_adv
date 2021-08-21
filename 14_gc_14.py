import time
import sys
class test:
    def __ini__(self):
        print("object initialization")
t1=test()
print(sys.getrefcount(t1))

import time
import gc
class test:
    def __init__(self):
        print("object intialization")
    def __del__(self):
        print("fulfilling last wish and performing cleaup activity")
t1=test()
t2=t1
t3=t2
t4=t3

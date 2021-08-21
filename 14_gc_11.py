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
del t1
time.sleep(5)
print("After deleting t1 object not destroyed")
del t2
del t3
time.sleep(5)
print("still object is not eligible for gc")
time.sleep(5)
del t4
time.sleep(10)
print("End of application")


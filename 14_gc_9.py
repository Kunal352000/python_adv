import time
import gc
class test:
    def __init__(self):
        print("object intialization")
    def __del__(self):
        print("fulfilling last wish and performing cleaup activity")
gc.disable()
print(gc.isenabled())#False
t1=test()
time.sleep(5)
print("End of application")

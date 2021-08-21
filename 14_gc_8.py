import time
import gc
class test:
    def __init__(self):
        print("object intizaltion")
    def __del__(self):
        print("fulfilling last wish and performing cleanup activity.")
gc.disable()
print(gc.isenabled())#False
t1=test()
t1=None
time.sleep(7)
print("End of application")

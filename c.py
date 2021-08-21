import time
import gc
class test:
    def __init__(self):
        print("object intizalization")
    def __del__(self):
        print("fulfiling last wish and performing cleaup activity")
gc.disable()
print(gc.isenabled())
t1=test()
t1=None
time.sleep(5)
print("stop")
